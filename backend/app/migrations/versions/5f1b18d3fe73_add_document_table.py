"""Add document table

Revision ID: 5f1b18d3fe73
Revises: c5420fc7c295
Create Date: 2024-08-22 15:43:09.114013

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "5f1b18d3fe73"
down_revision: Union[str, None] = "c5420fc7c295"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "document",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("external_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("source", sa.Enum("SLACK", name="documentsource"), nullable=False),
        sa.Column("title", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("content", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "doc_metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("embedding", postgresql.ARRAY(sa.FLOAT()), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_document_external_id"), "document", ["external_id"], unique=True
    )
    op.create_index(op.f("ix_document_title"), "document", ["title"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_document_title"), table_name="document")
    op.drop_index(op.f("ix_document_external_id"), table_name="document")
    op.drop_table("document")
    # ### end Alembic commands ###
