"""Add initial migration

Revision ID: 53daac222138
Revises: 
Create Date: 2024-08-24 21:38:20.347160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '53daac222138'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alertconfiguration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('query', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('provider', sa.Enum('DATADOG', name='alertsource'), nullable=True),
    sa.Column('provider_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_noisy', sa.Boolean(), nullable=False),
    sa.Column('noisy_reason', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alertconfiguration_name'), 'alertconfiguration', ['name'], unique=False)
    op.create_index(op.f('ix_alertconfiguration_provider_id'), 'alertconfiguration', ['provider_id'], unique=True)
    op.create_table('alert',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('severity', sa.Enum('LOW', 'MEDIUM', 'HIGH', 'CRITICAL', name='severitylevel'), nullable=True),
    sa.Column('status', sa.Enum('OPEN', 'RESOLVED', 'ACKNOWLEDGED', 'SUPPRESSED', name='alertstatus'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('alert_source', sa.Enum('DATADOG', name='alertsource'), nullable=True),
    sa.Column('tags', sa.JSON(), nullable=True),
    sa.Column('service', sa.String(), nullable=True),
    sa.Column('env', sa.String(), nullable=True),
    sa.Column('additional_data', sa.JSON(), nullable=True),
    sa.Column('provider_event_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('provider_aggregation_key', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('provider_cycle_key', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('duration_seconds', sa.Integer(), nullable=True),
    sa.Column('configuration_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['configuration_id'], ['alertconfiguration.provider_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alert_title'), 'alert', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_alert_title'), table_name='alert')
    op.drop_table('alert')
    op.drop_index(op.f('ix_alertconfiguration_provider_id'), table_name='alertconfiguration')
    op.drop_index(op.f('ix_alertconfiguration_name'), table_name='alertconfiguration')
    op.drop_table('alertconfiguration')
    # ### end Alembic commands ###
