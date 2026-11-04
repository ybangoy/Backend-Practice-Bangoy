from sqlmodel import Field , SQLModel

class Retail(SQLModel, table=True):
    compid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    loc: str
    established_date: int | None = None

class Crew(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    age: int | None = None
    salary: int | None = None

class Order(SQLModel, table=True):
    orderid: int | None = Field(default=None, primary_key=True)
    ordernumber: str
    productname: str
    prodnumber: int | None = None
    time: str