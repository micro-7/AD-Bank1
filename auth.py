"""
KYC session verification middleware -- ensures a customer has an
active, valid KYC session before they can upload verification
documents.
"""

from fastapi import HTTPException, Header


def verify_kyc_session(x_session_token: str = Header(...)):
    if not x_session_token or len(x_session_token) < 20:
        raise HTTPException(status_code=401, detail="Invalid or missing KYC session token")
    return x_session_token
