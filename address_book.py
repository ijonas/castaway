from sqlalchemy import create_engine, Column, String, select
from sqlalchemy.orm import declarative_base, Session
import os

# Create db directory if it doesn't exist
os.makedirs("db", exist_ok=True)

# Setup the database
engine = create_engine("sqlite:///db/address_book.sqlite")
Base = declarative_base()

class Address(Base):
    """SQLAlchemy model for an address record."""
    __tablename__ = "addresses"
    
    name = Column(String, primary_key=True)
    evm_address = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Address(name={self.name}, evm_address={self.evm_address})"

# Create tables if they don't exist
Base.metadata.create_all(engine)

def add_address(name: str, evm_address: str) -> str:
    """Add a new address to the address book."""
    with Session(engine) as session:
        # Check if address with this name already exists
        existing = session.execute(
            select(Address).where(Address.name == name)
        ).first()
        
        if existing:
            return f"Address with name '{name}' already exists"
        
        # Create new address
        address = Address(name=name, evm_address=evm_address)
        session.add(address)
        session.commit()
        return f"Added address {name}: {evm_address}"

def get_address(name: str) -> str:
    """Get an address by name."""
    with Session(engine) as session:
        address = session.execute(
            select(Address).where(Address.name == name)
        ).scalar_one_or_none()
        
        if not address:
            return f"No address found with name '{name}'"
        
        return address.evm_address

def get_all_addresses() -> dict:
    """Get all addresses in the address book."""
    with Session(engine) as session:
        addresses = session.execute(select(Address)).scalars().all()
        return {address.name: address.evm_address for address in addresses}

def update_address(name: str, evm_address: str) -> str:
    """Update an existing address."""
    with Session(engine) as session:
        address = session.execute(
            select(Address).where(Address.name == name)
        ).scalar_one_or_none()
        
        if not address:
            return f"No address found with name '{name}'"
        
        address.evm_address = evm_address
        session.commit()
        return f"Updated address {name}: {evm_address}"

def delete_address(name: str) -> str:
    """Delete an address from the address book."""
    with Session(engine) as session:
        address = session.execute(
            select(Address).where(Address.name == name)
        ).scalar_one_or_none()
        
        if not address:
            return f"No address found with name '{name}'"
        
        session.delete(address)
        session.commit()
        return f"Deleted address '{name}'"