# Interface ManagerFactoryParameters

**Source:** `java.base\javax\net\ssl\ManagerFactoryParameters.html`

### Class Description

```java
public interface
ManagerFactoryParameters
```

This class is the base interface for providing
algorithm-specific information to a KeyManagerFactory or
TrustManagerFactory.

In some cases, initialization parameters other than keystores
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate
sub-interface of this class as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

**All Known Implementing Classes:** CertPathTrustManagerParameters

,

KeyStoreBuilderParameters

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface ManagerFactoryParameters

**All Known Implementing Classes:** CertPathTrustManagerParameters

,

KeyStoreBuilderParameters

```java
public interface
ManagerFactoryParameters
```

This class is the base interface for providing
algorithm-specific information to a KeyManagerFactory or
TrustManagerFactory.

In some cases, initialization parameters other than keystores
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate
sub-interface of this class as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

**Since:** 1.4

public interface

ManagerFactoryParameters

This class is the base interface for providing
algorithm-specific information to a KeyManagerFactory or
TrustManagerFactory.

In some cases, initialization parameters other than keystores
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate
sub-interface of this class as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

In some cases, initialization parameters other than keystores
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate
sub-interface of this class as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

---

