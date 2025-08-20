
# Modelo de bando de dados usando sqlalchemy, é uma bliblioteca ORM para Python que transforma tabelas de banco de dados em classes Python.

# Objetivo é criar duas tabelas de banco de dados postgresql:
    # tabela targets: guardar os sites que queremos monitorar
        #cada linha da tabela é um site
        # campos: id, url, enabled, created_at
    # tabela checks: guardar os resultados feitos nos sites
        # campos: id, target_id, ts, status, latency, error_message

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, func

class Base(DeclarativeBase):
    pass

class Target(Base):
    __tablename__ = "targets"
    
    id: Mapped[int] = mapped_column(primary_key=True) # numero unico da linha
    url: Mapped[str] = mapped_column(String, unique=True, nullable=False) # url do site a ser monitorado
    enabled: Mapped[bool] = mapped_column(Boolean, default=True) # se o site está habilitado para monitoramento
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now()) # data de criação do registro
    
    checks: Mapped[list["Check"]] = relationship(back_populates="target")  # relacionamento com a tabela de checks
    
class Check(Base):
    __tablename__ = "checks"
    
    id: Mapped[int] = mapped_column(primary_key=True) # numero unico da linha
    target_id: Mapped[int] = mapped_column(ForeignKey("targets.id", ondelete="CASCADE")) #aponta para targetid da tabela targets
    ts: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now()) # data e hora do check
    status: Mapped[int] = mapped_column() # status do check (ex: "up", "down")
    latency_ms: Mapped[int] = mapped_column() # latência do check em milissegundos
    error: Mapped[Optional[str]] = mapped_column(nullable=True) # mensagem de erro, se houver
    
    target: Mapped[Target] = relationship(back_populates="checks")  # cria o caminho reverso target.checks