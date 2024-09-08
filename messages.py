from base64 import urlsafe_b64encode

from pytoniq_core import begin_cell


def get_comment_message() -> dict:

    data = {
        'address': 'EQADI20e2GyGwacUurQ-d7mHY3jd4WMDyMsBoUpVoHvbnai8',
        'amount': str(int(0.16*1e9)),
        'payload': urlsafe_b64encode(
            begin_cell()
            .store_uint(0x6de123ea, 32)
            .store_uint(999, 64)  # op code for comment message
            .end_cell()  # end cell
            .to_boc()  # convert it to boc
        )
        .decode()  # encode it to urlsafe base64
    }

    return data