"""initial migration

Revision ID: 00ae1378de91
Revises: 1d7377ea5e93
Create Date: 2024-10-16 19:58:09.297325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import models

# revision identifiers, used by Alembic.
revision: str = '00ae1378de91'
down_revision: Union[str, None] = '1d7377ea5e93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
