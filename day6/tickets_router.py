from fastapi import APIRouter, HTTPException
import database
from schemas import TicketCreate, TicketStatusUpdate

router = APIRouter(prefix="/tickets", tags=["tickets"])