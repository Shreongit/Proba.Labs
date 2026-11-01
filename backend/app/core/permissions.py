
from enum import StrEnum

from app.core.exceptions import PermissionDeniedException


class WorkspaceRole(StrEnum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"
    VIEWER = "viewer"


ROLE_PERMISSIONS: dict[WorkspaceRole, set[str]] = {
    WorkspaceRole.OWNER: {
        "workspace:manage",
        "workspace:delete",
        "members:manage",
        "projects:create",
        "projects:read",
        "projects:update",
        "projects:delete",
        "models:manage",
        "datasets:manage",
        "experiments:manage",
        "reports:read",
    },
    WorkspaceRole.ADMIN: {
        "workspace:manage",
        "members:manage",
        "projects:create",
        "projects:read",
        "projects:update",
        "projects:delete",
        "models:manage",
        "datasets:manage",
        "experiments:manage",
        "reports:read",
    },
    WorkspaceRole.MEMBER: {
        "projects:create",
        "projects:read",
        "projects:update",
        "models:manage",
        "datasets:manage",
        "experiments:manage",
        "reports:read",
    },
    WorkspaceRole.VIEWER: {
        "projects:read",
        "reports:read",
    },
}


def has_permission(role: WorkspaceRole, permission: str) -> bool:
    """Check whether a workspace role has a permission."""
    return permission in ROLE_PERMISSIONS.get(role, set())


def require_permission(role: WorkspaceRole, permission: str) -> None:
    """Raise an exception when a role lacks a permission."""
    if not has_permission(role, permission):
        raise PermissionDeniedException(
            f"Role '{role.value}' cannot perform '{permission}'."
        )
