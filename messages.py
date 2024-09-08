from pytoniq_core import begin_cell, HashMap
from base64 import urlsafe_b64encode
import requests

base_url = "http://localhost:3010/api/merkle/proof/"


def get_comment_message(id) -> dict:
    url = f"{base_url}{id}"
    response = requests.get(url)
    data = response.json()

    proof = data.get("proof", [])
    depth = data.get("depth")
    leaf = int(data.get("leaf"))
    leaf_index = id

    hashmap = HashMap(key_size=32, value_serializer=lambda src, dest: dest.store_uint(src, 256))
    i = 0
    for hash in proof:
        hashmap.set(key=i, value=int(hash))
        i += 1

    pdb = begin_cell().store_dict(hashmap.serialize()).end_cell()

    data = {
        'address': 'EQBlmBj9ObTrZ12wWVRNzTiURj0gpYgCenmDH4oc4s7-SOaf',
        'amount': str(int(0.05 * 1e9)),
        'payload': urlsafe_b64encode(
            begin_cell()
            .store_uint(0x8e8764cc, 32)
            .store_cell(pdb)
            .store_uint(leaf, 32)
            .store_uint(leaf_index, 32)
            .end_cell()  # end cell
            .to_boc()  # convert it to boc
        )
        .decode()  # encode it to urlsafe base64
    }

    return data
print(get_comment_message(0))