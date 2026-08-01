from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.auth.auth import get_current_user
from app.models.user import User

from app.crud.vendor import (
    create_vendor,
    get_vendor,
    get_all_vendors,
    update_vendor,
    delete_vendor,
)

from app.schemas.vendor import (
    VendorCreate,
    VendorUpdate,
    VendorResponse,
)


router = APIRouter(
    prefix="/vendors",
    tags=["Vendors"],
)



# CREATE VENDOR
@router.post(
    "/",
    response_model=VendorResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_vendor_api(
    vendor: VendorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_vendor(
        db,
        vendor
    )



# GET ALL VENDORS
@router.get(
    "/",
    response_model=List[VendorResponse],
)
def get_all_vendors_api(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_vendors(db)



# GET SINGLE VENDOR
@router.get(
    "/{vendor_id}",
    response_model=VendorResponse,
)
def get_vendor_api(
    vendor_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    vendor = get_vendor(
        db,
        vendor_id
    )


    if vendor is None:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )


    return vendor




# UPDATE VENDOR
@router.put(
    "/{vendor_id}",
    response_model=VendorResponse,
)
def update_vendor_api(
    vendor_id: int,
    vendor_update: VendorUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    db_vendor = get_vendor(
        db,
        vendor_id
    )


    if db_vendor is None:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )


    return update_vendor(
        db,
        db_vendor,
        vendor_update
    )




# DELETE VENDOR
@router.delete(
    "/{vendor_id}",
)
def delete_vendor_api(
    vendor_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    db_vendor = get_vendor(
        db,
        vendor_id
    )


    if db_vendor is None:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )


    delete_vendor(
        db,
        db_vendor
    )


    return {
        "message": "Vendor deleted successfully"
    }

# --------------------------------
# Vendor List
# --------------------------------

@router.get("/")
def vendors(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):


    return get_all_vendors(db)



# --------------------------------
# Vendor Analytics
# --------------------------------

@router.get("/{vendor_id}/analytics")
def vendor_analytics(

    vendor_id:int,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):


    return get_vendor_statistics(

        db,

        vendor_id

    )