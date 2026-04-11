# Interface ExtendedGSSCredential

**Source:** `jdk.security.jgss\com\sun\security\jgss\ExtendedGSSCredential.html`

### Class Description

```java
public interface
ExtendedGSSCredential

extends
GSSCredential
```

The extended GSSCredential interface for supporting additional
functionalities not defined by

org.ietf.jgss.GSSCredential

.

**All Superinterfaces:** Cloneable

,

GSSCredential

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### GSSCredential
impersonate​(
GSSName
name)
throws
GSSException

Impersonates a principal. In Kerberos, this can be implemented
using the Microsoft S4U2self extension.

A

GSSException.NO_CRED

will be thrown if the
impersonation fails. A

GSSException.FAILURE

will be thrown if the impersonation method is not available to this
credential object.

**Parameters:**
- name

- the name of the principal to impersonate

**Returns:**
- a credential for that principal

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.NO_CRED

GSSException.FAILURE

---

### Additional Sections

#### Interface ExtendedGSSCredential

**All Superinterfaces:** Cloneable

,

GSSCredential

```java
public interface
ExtendedGSSCredential

extends
GSSCredential
```

The extended GSSCredential interface for supporting additional
functionalities not defined by

org.ietf.jgss.GSSCredential

.

**Since:** 1.8

public interface

ExtendedGSSCredential

extends

GSSCredential

The extended GSSCredential interface for supporting additional
functionalities not defined by

org.ietf.jgss.GSSCredential

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface org.ietf.jgss.

GSSCredential

ACCEPT_ONLY

,

DEFAULT_LIFETIME

,

INDEFINITE_LIFETIME

,

INITIATE_AND_ACCEPT

,

INITIATE_ONLY

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

GSSCredential

impersonate

​(

GSSName

name)

Impersonates a principal.

- Methods declared in interface org.ietf.jgss.

GSSCredential

add

,

dispose

,

equals

,

getMechs

,

getName

,

getName

,

getRemainingAcceptLifetime

,

getRemainingInitLifetime

,

getRemainingLifetime

,

getUsage

,

getUsage

,

hashCode

Field Summary

- Fields declared in interface org.ietf.jgss.

GSSCredential

ACCEPT_ONLY

,

DEFAULT_LIFETIME

,

INDEFINITE_LIFETIME

,

INITIATE_AND_ACCEPT

,

INITIATE_ONLY

---

#### Field Summary

Fields declared in interface org.ietf.jgss.

GSSCredential

ACCEPT_ONLY

,

DEFAULT_LIFETIME

,

INDEFINITE_LIFETIME

,

INITIATE_AND_ACCEPT

,

INITIATE_ONLY

---

#### Fields declared in interface org.ietf.jgss. GSSCredential

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

GSSCredential

impersonate

​(

GSSName

name)

Impersonates a principal.

- Methods declared in interface org.ietf.jgss.

GSSCredential

add

,

dispose

,

equals

,

getMechs

,

getName

,

getName

,

getRemainingAcceptLifetime

,

getRemainingInitLifetime

,

getRemainingLifetime

,

getUsage

,

getUsage

,

hashCode

---

#### Method Summary

Impersonates a principal.

Methods declared in interface org.ietf.jgss.

GSSCredential

add

,

dispose

,

equals

,

getMechs

,

getName

,

getName

,

getRemainingAcceptLifetime

,

getRemainingInitLifetime

,

getRemainingLifetime

,

getUsage

,

getUsage

,

hashCode

---

#### Methods declared in interface org.ietf.jgss. GSSCredential

============ METHOD DETAIL ==========

- Method Detail

- impersonate

```java
GSSCredential
impersonate​(
GSSName
name)
throws
GSSException
```

Impersonates a principal. In Kerberos, this can be implemented
using the Microsoft S4U2self extension.

A

GSSException.NO_CRED

will be thrown if the
impersonation fails. A

GSSException.FAILURE

will be thrown if the impersonation method is not available to this
credential object.

**Parameters:** name

- the name of the principal to impersonate
**Returns:** a credential for that principal
**Throws:** GSSException

- containing the following
major error codes:

GSSException.NO_CRED

GSSException.FAILURE

Method Detail

- impersonate

```java
GSSCredential
impersonate​(
GSSName
name)
throws
GSSException
```

Impersonates a principal. In Kerberos, this can be implemented
using the Microsoft S4U2self extension.

A

GSSException.NO_CRED

will be thrown if the
impersonation fails. A

GSSException.FAILURE

will be thrown if the impersonation method is not available to this
credential object.

**Parameters:** name

- the name of the principal to impersonate
**Returns:** a credential for that principal
**Throws:** GSSException

- containing the following
major error codes:

GSSException.NO_CRED

GSSException.FAILURE

---

#### Method Detail

impersonate

```java
GSSCredential
impersonate​(
GSSName
name)
throws
GSSException
```

Impersonates a principal. In Kerberos, this can be implemented
using the Microsoft S4U2self extension.

A

GSSException.NO_CRED

will be thrown if the
impersonation fails. A

GSSException.FAILURE

will be thrown if the impersonation method is not available to this
credential object.

**Parameters:** name

- the name of the principal to impersonate
**Returns:** a credential for that principal
**Throws:** GSSException

- containing the following
major error codes:

GSSException.NO_CRED

GSSException.FAILURE

---

#### impersonate

GSSCredential

impersonate​(

GSSName

name)
throws

GSSException

Impersonates a principal. In Kerberos, this can be implemented
using the Microsoft S4U2self extension.

A

GSSException.NO_CRED

will be thrown if the
impersonation fails. A

GSSException.FAILURE

will be thrown if the impersonation method is not available to this
credential object.

A

GSSException.NO_CRED

will be thrown if the
impersonation fails. A

GSSException.FAILURE

will be thrown if the impersonation method is not available to this
credential object.

---

