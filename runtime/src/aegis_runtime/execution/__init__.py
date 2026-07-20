"""Execution foundation for Aegis OS runtime."""


from .audit import (
    ExecutionAuditEvent,
    ExecutionAuditEventType,
)
from .audit_authentication import (
    AUDIT_AUTHENTICATION_ALGORITHM,
    AUDIT_AUTHENTICATION_CONTEXT,
    AUDIT_AUTHENTICATION_MINIMUM_KEY_BYTES,
    AUDIT_AUTHENTICATION_VERSION,
    ExecutionAuditAuthenticationVerification,
    ExecutionAuditAuthenticator,
)
from .audit_authentication_config import (
    AUDIT_HMAC_DEFAULT_KEY_ID,
    AUDIT_HMAC_KEY_ID_ENV,
    AUDIT_HMAC_SECRET_ENV,
    AUDIT_HMAC_SECRET_FILE_ENV,
    ExecutionAuditAuthenticationConfig,
)
from .audit_history import (
    ExecutionAuditHistory,
    ExecutionAuditHistoryReader,
)
from .audit_integrity import (
    AUDIT_GENESIS_HASH,
    AUDIT_INTEGRITY_ALGORITHM,
    AUDIT_INTEGRITY_VERSION,
    ExecutionAuditIntegrity,
    ExecutionAuditIntegrityVerification,
)
from .audit_protection import (
    ExecutionAuditProtection,
    ExecutionAuditProtectionVerification,
)
from .audit_verification import (
    ExecutionAuditVerificationReport,
    ExecutionAuditVerifier,
)
from .context import (
    ExecutionArtifact,
    ExecutionContext,
    ExecutionEnvironment,
    ResolvedExecutionInput,
)
from .context_builder import (
    ContextBuildIssue,
    ExecutionContextBuilder,
    ExecutionContextBuildResult,
)
from .contract_builder import ExecutionContractBuilder
from .contract_validator import ExecutionContractValidator
from .contracts import (
    ContractValidationIssue,
    ContractValidationResult,
    ExecutionContract,
    ExecutionContractType,
    ExecutionInput,
    ExecutionOutput,
    ExecutionSafetyLevel,
)
from .input_resolver import (
    ExecutionInputResolver,
    InputResolutionIssue,
    InputResolutionResult,
)
from .lifecycle import (
    ExecutionLifecycleAction,
    ExecutionLifecycleManager,
    ExecutionLifecycleResult,
)
from .lifecycle_store import (
    ExecutionLifecycleStore,
    PersistedExecutionLifecycle,
)
from .models import (
    ExecutionMode,
    ExecutionPlan,
    ExecutionReport,
    ExecutionStatus,
    ExecutionStep,
)
from .orchestrator import (
    ExecutionOrchestrationResult,
    ExecutionOrchestrator,
)
from .orchestration_store import (
    ExecutionOrchestrationStore,
    PersistedExecutionOrchestration,
)
from .session import (
    ExecutionSession,
    ExecutionSessionState,
)
from .session_builder import (
    ExecutionSessionBuilder,
    ExecutionSessionBuildResult,
    SessionBuildIssue,
)
from .session_loader import ExecutionSessionLoader
from .workspace import (
    ExecutionWorkspace,
    ExecutionWorkspaceState,
    WorkspaceLocation,
)
from .workspace_store import (
    ExecutionWorkspaceStore,
    PersistedExecutionWorkspace,
    StoredExecutionSession,
)

__all__ = [
    "AUDIT_AUTHENTICATION_ALGORITHM",
    "AUDIT_AUTHENTICATION_CONTEXT",
    "AUDIT_AUTHENTICATION_MINIMUM_KEY_BYTES",
    "AUDIT_AUTHENTICATION_VERSION",
    "AUDIT_GENESIS_HASH",
    "AUDIT_HMAC_DEFAULT_KEY_ID",
    "AUDIT_HMAC_KEY_ID_ENV",
    "AUDIT_HMAC_SECRET_ENV",
    "AUDIT_HMAC_SECRET_FILE_ENV",
    "AUDIT_INTEGRITY_ALGORITHM",
    "AUDIT_INTEGRITY_VERSION",
    "ContextBuildIssue",
    "ContractValidationIssue",
    "ContractValidationResult",
    "ExecutionArtifact",
    "ExecutionAuditAuthenticationConfig",
    "ExecutionAuditAuthenticationVerification",
    "ExecutionAuditAuthenticator",
    "ExecutionAuditEvent",
    "ExecutionAuditEventType",
    "ExecutionAuditHistory",
    "ExecutionAuditHistoryReader",
    "ExecutionAuditIntegrity",
    "ExecutionAuditIntegrityVerification",
    "ExecutionAuditProtection",
    "ExecutionAuditProtectionVerification",
    "ExecutionAuditVerificationReport",
    "ExecutionAuditVerifier",
    "ExecutionContext",
    "ExecutionContextBuilder",
    "ExecutionContextBuildResult",
    "ExecutionContract",
    "ExecutionContractBuilder",
    "ExecutionContractType",
    "ExecutionContractValidator",
    "ExecutionEnvironment",
    "ExecutionInput",
    "ExecutionInputResolver",
    "ExecutionLifecycleAction",
    "ExecutionLifecycleManager",
    "ExecutionLifecycleResult",
    "ExecutionLifecycleStore",
    "ExecutionMode",
    "ExecutionOrchestrationResult",
    "ExecutionOrchestrator",
    "ExecutionOrchestrationStore",
    "ExecutionOutput",
    "ExecutionPlan",
    "ExecutionReport",
    "ExecutionSafetyLevel",
    "ExecutionSession",
    "ExecutionSessionBuilder",
    "ExecutionSessionBuildResult",
    "ExecutionSessionLoader",
    "ExecutionSessionState",
    "ExecutionStatus",
    "ExecutionStep",
    "ExecutionWorkspace",
    "ExecutionWorkspaceState",
    "ExecutionWorkspaceStore",
    "InputResolutionIssue",
    "InputResolutionResult",
    "PersistedExecutionLifecycle",
    "PersistedExecutionOrchestration",
    "PersistedExecutionWorkspace",
    "ResolvedExecutionInput",
    "SessionBuildIssue",
    "StoredExecutionSession",
    "WorkspaceLocation",
]