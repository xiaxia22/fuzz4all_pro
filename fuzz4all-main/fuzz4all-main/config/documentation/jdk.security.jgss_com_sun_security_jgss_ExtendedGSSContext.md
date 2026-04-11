# Interface ExtendedGSSContext

**Source:** `jdk.security.jgss\com\sun\security\jgss\ExtendedGSSContext.html`

### Class Description

```java
public interface
ExtendedGSSContext

extends
GSSContext
```

The extended GSSContext interface for supporting additional
functionalities not defined by

org.ietf.jgss.GSSContext

,
such as querying context-specific attributes.

**All Superinterfaces:** GSSContext

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
inquireSecContext​(
InquireType
type)
throws
GSSException

Return the mechanism-specific attribute associated with

type

.

If there is a security manager, an

InquireSecContextPermission

with the name

type.mech

must be granted. Otherwise, this could
result in a

SecurityException

.

Example:

```java
GSSContext ctxt = m.createContext(...)
// Establishing the context
if (ctxt instanceof ExtendedGSSContext) {
ExtendedGSSContext ex = (ExtendedGSSContext)ctxt;
try {
Key key = (key)ex.inquireSecContext(
InquireType.KRB5_GET_SESSION_KEY);
// read key info
} catch (GSSException gsse) {
// deal with exception
}
}
```

**Parameters:**
- type

- the type of the attribute requested

**Returns:**
- the attribute, see the method documentation for details.

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

if the mechanism
does not support this method,

GSSException.UNAVAILABLE

if the
type specified is not supported,

GSSException.NO_CONTEXT

if the
security context is invalid,

GSSException.FAILURE

for other
unspecified failures.
- SecurityException

- if a security manager exists and a proper

InquireSecContextPermission

is not granted.

**See Also:**
- InquireSecContextPermission

,

InquireType

---

#### void requestDelegPolicy​(boolean state)
throws
GSSException

Requests that the delegation policy be respected. When a true value is
requested, the underlying context would use the delegation policy
defined by the environment as a hint to determine whether credentials
delegation should be performed. This request can only be made on the
context initiator's side and it has to be done prior to the first
call to

initSecContext

.

When this flag is false, delegation will only be tried when the

credentials delegation flag

is true.

When this flag is true but the

credentials delegation flag

is false, delegation will be only tried if the delegation policy permits
delegation.

When both this flag and the

credentials delegation flag

are true, delegation will be always tried. However, if the delegation
policy does not permit delegation, the value of

getDelegPolicyState()

will be false, even
if delegation is performed successfully.

In any case, if the delegation is not successful, the value returned
by

GSSContext.getCredDelegState()

is false, and the value
returned by

getDelegPolicyState()

is also false.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

**Parameters:**
- state

- true if the policy should be respected

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### boolean getDelegPolicyState()

Returns the delegation policy response. Called after a security context
is established. This method can be only called on the initiator's side.
See

requestDelegPolicy(boolean)

.

**Returns:**
- the delegation policy response

---

### Additional Sections

#### Interface ExtendedGSSContext

**All Superinterfaces:** GSSContext

```java
public interface
ExtendedGSSContext

extends
GSSContext
```

The extended GSSContext interface for supporting additional
functionalities not defined by

org.ietf.jgss.GSSContext

,
such as querying context-specific attributes.

public interface

ExtendedGSSContext

extends

GSSContext

The extended GSSContext interface for supporting additional
functionalities not defined by

org.ietf.jgss.GSSContext

,
such as querying context-specific attributes.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface org.ietf.jgss.

GSSContext

DEFAULT_LIFETIME

,

INDEFINITE_LIFETIME

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getDelegPolicyState

()

Returns the delegation policy response.

Object

inquireSecContext

​(

InquireType

type)

Return the mechanism-specific attribute associated with

type

.

void

requestDelegPolicy

​(boolean state)

Requests that the delegation policy be respected.

- Methods declared in interface org.ietf.jgss.

GSSContext

acceptSecContext

,

acceptSecContext

,

dispose

,

export

,

getAnonymityState

,

getConfState

,

getCredDelegState

,

getDelegCred

,

getIntegState

,

getLifetime

,

getMech

,

getMIC

,

getMIC

,

getMutualAuthState

,

getReplayDetState

,

getSequenceDetState

,

getSrcName

,

getTargName

,

getWrapSizeLimit

,

initSecContext

,

initSecContext

,

isEstablished

,

isInitiator

,

isProtReady

,

isTransferable

,

requestAnonymity

,

requestConf

,

requestCredDeleg

,

requestInteg

,

requestLifetime

,

requestMutualAuth

,

requestReplayDet

,

requestSequenceDet

,

setChannelBinding

,

unwrap

,

unwrap

,

verifyMIC

,

verifyMIC

,

wrap

,

wrap

Field Summary

- Fields declared in interface org.ietf.jgss.

GSSContext

DEFAULT_LIFETIME

,

INDEFINITE_LIFETIME

---

#### Field Summary

Fields declared in interface org.ietf.jgss.

GSSContext

DEFAULT_LIFETIME

,

INDEFINITE_LIFETIME

---

#### Fields declared in interface org.ietf.jgss. GSSContext

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getDelegPolicyState

()

Returns the delegation policy response.

Object

inquireSecContext

​(

InquireType

type)

Return the mechanism-specific attribute associated with

type

.

void

requestDelegPolicy

​(boolean state)

Requests that the delegation policy be respected.

- Methods declared in interface org.ietf.jgss.

GSSContext

acceptSecContext

,

acceptSecContext

,

dispose

,

export

,

getAnonymityState

,

getConfState

,

getCredDelegState

,

getDelegCred

,

getIntegState

,

getLifetime

,

getMech

,

getMIC

,

getMIC

,

getMutualAuthState

,

getReplayDetState

,

getSequenceDetState

,

getSrcName

,

getTargName

,

getWrapSizeLimit

,

initSecContext

,

initSecContext

,

isEstablished

,

isInitiator

,

isProtReady

,

isTransferable

,

requestAnonymity

,

requestConf

,

requestCredDeleg

,

requestInteg

,

requestLifetime

,

requestMutualAuth

,

requestReplayDet

,

requestSequenceDet

,

setChannelBinding

,

unwrap

,

unwrap

,

verifyMIC

,

verifyMIC

,

wrap

,

wrap

---

#### Method Summary

Returns the delegation policy response.

Return the mechanism-specific attribute associated with

type

.

Requests that the delegation policy be respected.

Methods declared in interface org.ietf.jgss.

GSSContext

acceptSecContext

,

acceptSecContext

,

dispose

,

export

,

getAnonymityState

,

getConfState

,

getCredDelegState

,

getDelegCred

,

getIntegState

,

getLifetime

,

getMech

,

getMIC

,

getMIC

,

getMutualAuthState

,

getReplayDetState

,

getSequenceDetState

,

getSrcName

,

getTargName

,

getWrapSizeLimit

,

initSecContext

,

initSecContext

,

isEstablished

,

isInitiator

,

isProtReady

,

isTransferable

,

requestAnonymity

,

requestConf

,

requestCredDeleg

,

requestInteg

,

requestLifetime

,

requestMutualAuth

,

requestReplayDet

,

requestSequenceDet

,

setChannelBinding

,

unwrap

,

unwrap

,

verifyMIC

,

verifyMIC

,

wrap

,

wrap

---

#### Methods declared in interface org.ietf.jgss. GSSContext

============ METHOD DETAIL ==========

- Method Detail

- inquireSecContext

```java
Object
inquireSecContext​(
InquireType
type)
throws
GSSException
```

Return the mechanism-specific attribute associated with

type

.

If there is a security manager, an

InquireSecContextPermission

with the name

type.mech

must be granted. Otherwise, this could
result in a

SecurityException

.

Example:

```java
GSSContext ctxt = m.createContext(...)
// Establishing the context
if (ctxt instanceof ExtendedGSSContext) {
ExtendedGSSContext ex = (ExtendedGSSContext)ctxt;
try {
Key key = (key)ex.inquireSecContext(
InquireType.KRB5_GET_SESSION_KEY);
// read key info
} catch (GSSException gsse) {
// deal with exception
}
}
```

**Parameters:** type

- the type of the attribute requested
**Returns:** the attribute, see the method documentation for details.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

if the mechanism
does not support this method,

GSSException.UNAVAILABLE

if the
type specified is not supported,

GSSException.NO_CONTEXT

if the
security context is invalid,

GSSException.FAILURE

for other
unspecified failures.
**Throws:** SecurityException

- if a security manager exists and a proper

InquireSecContextPermission

is not granted.
**See Also:** InquireSecContextPermission

,

InquireType

- requestDelegPolicy

```java
void requestDelegPolicy​(boolean state)
throws
GSSException
```

Requests that the delegation policy be respected. When a true value is
requested, the underlying context would use the delegation policy
defined by the environment as a hint to determine whether credentials
delegation should be performed. This request can only be made on the
context initiator's side and it has to be done prior to the first
call to

initSecContext

.

When this flag is false, delegation will only be tried when the

credentials delegation flag

is true.

When this flag is true but the

credentials delegation flag

is false, delegation will be only tried if the delegation policy permits
delegation.

When both this flag and the

credentials delegation flag

are true, delegation will be always tried. However, if the delegation
policy does not permit delegation, the value of

getDelegPolicyState()

will be false, even
if delegation is performed successfully.

In any case, if the delegation is not successful, the value returned
by

GSSContext.getCredDelegState()

is false, and the value
returned by

getDelegPolicyState()

is also false.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

**Parameters:** state

- true if the policy should be respected
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- getDelegPolicyState

```java
boolean getDelegPolicyState()
```

Returns the delegation policy response. Called after a security context
is established. This method can be only called on the initiator's side.
See

requestDelegPolicy(boolean)

.

**Returns:** the delegation policy response

Method Detail

- inquireSecContext

```java
Object
inquireSecContext​(
InquireType
type)
throws
GSSException
```

Return the mechanism-specific attribute associated with

type

.

If there is a security manager, an

InquireSecContextPermission

with the name

type.mech

must be granted. Otherwise, this could
result in a

SecurityException

.

Example:

```java
GSSContext ctxt = m.createContext(...)
// Establishing the context
if (ctxt instanceof ExtendedGSSContext) {
ExtendedGSSContext ex = (ExtendedGSSContext)ctxt;
try {
Key key = (key)ex.inquireSecContext(
InquireType.KRB5_GET_SESSION_KEY);
// read key info
} catch (GSSException gsse) {
// deal with exception
}
}
```

**Parameters:** type

- the type of the attribute requested
**Returns:** the attribute, see the method documentation for details.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

if the mechanism
does not support this method,

GSSException.UNAVAILABLE

if the
type specified is not supported,

GSSException.NO_CONTEXT

if the
security context is invalid,

GSSException.FAILURE

for other
unspecified failures.
**Throws:** SecurityException

- if a security manager exists and a proper

InquireSecContextPermission

is not granted.
**See Also:** InquireSecContextPermission

,

InquireType

- requestDelegPolicy

```java
void requestDelegPolicy​(boolean state)
throws
GSSException
```

Requests that the delegation policy be respected. When a true value is
requested, the underlying context would use the delegation policy
defined by the environment as a hint to determine whether credentials
delegation should be performed. This request can only be made on the
context initiator's side and it has to be done prior to the first
call to

initSecContext

.

When this flag is false, delegation will only be tried when the

credentials delegation flag

is true.

When this flag is true but the

credentials delegation flag

is false, delegation will be only tried if the delegation policy permits
delegation.

When both this flag and the

credentials delegation flag

are true, delegation will be always tried. However, if the delegation
policy does not permit delegation, the value of

getDelegPolicyState()

will be false, even
if delegation is performed successfully.

In any case, if the delegation is not successful, the value returned
by

GSSContext.getCredDelegState()

is false, and the value
returned by

getDelegPolicyState()

is also false.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

**Parameters:** state

- true if the policy should be respected
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- getDelegPolicyState

```java
boolean getDelegPolicyState()
```

Returns the delegation policy response. Called after a security context
is established. This method can be only called on the initiator's side.
See

requestDelegPolicy(boolean)

.

**Returns:** the delegation policy response

---

#### Method Detail

inquireSecContext

```java
Object
inquireSecContext​(
InquireType
type)
throws
GSSException
```

Return the mechanism-specific attribute associated with

type

.

If there is a security manager, an

InquireSecContextPermission

with the name

type.mech

must be granted. Otherwise, this could
result in a

SecurityException

.

Example:

```java
GSSContext ctxt = m.createContext(...)
// Establishing the context
if (ctxt instanceof ExtendedGSSContext) {
ExtendedGSSContext ex = (ExtendedGSSContext)ctxt;
try {
Key key = (key)ex.inquireSecContext(
InquireType.KRB5_GET_SESSION_KEY);
// read key info
} catch (GSSException gsse) {
// deal with exception
}
}
```

**Parameters:** type

- the type of the attribute requested
**Returns:** the attribute, see the method documentation for details.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

if the mechanism
does not support this method,

GSSException.UNAVAILABLE

if the
type specified is not supported,

GSSException.NO_CONTEXT

if the
security context is invalid,

GSSException.FAILURE

for other
unspecified failures.
**Throws:** SecurityException

- if a security manager exists and a proper

InquireSecContextPermission

is not granted.
**See Also:** InquireSecContextPermission

,

InquireType

---

#### inquireSecContext

Object

inquireSecContext​(

InquireType

type)
throws

GSSException

Return the mechanism-specific attribute associated with

type

.

If there is a security manager, an

InquireSecContextPermission

with the name

type.mech

must be granted. Otherwise, this could
result in a

SecurityException

.

Example:

```java
GSSContext ctxt = m.createContext(...)
// Establishing the context
if (ctxt instanceof ExtendedGSSContext) {
ExtendedGSSContext ex = (ExtendedGSSContext)ctxt;
try {
Key key = (key)ex.inquireSecContext(
InquireType.KRB5_GET_SESSION_KEY);
// read key info
} catch (GSSException gsse) {
// deal with exception
}
}
```

If there is a security manager, an

InquireSecContextPermission

with the name

type.mech

must be granted. Otherwise, this could
result in a

SecurityException

.

Example:

```java
GSSContext ctxt = m.createContext(...)
// Establishing the context
if (ctxt instanceof ExtendedGSSContext) {
ExtendedGSSContext ex = (ExtendedGSSContext)ctxt;
try {
Key key = (key)ex.inquireSecContext(
InquireType.KRB5_GET_SESSION_KEY);
// read key info
} catch (GSSException gsse) {
// deal with exception
}
}
```

Example:

```java
GSSContext ctxt = m.createContext(...)
// Establishing the context
if (ctxt instanceof ExtendedGSSContext) {
ExtendedGSSContext ex = (ExtendedGSSContext)ctxt;
try {
Key key = (key)ex.inquireSecContext(
InquireType.KRB5_GET_SESSION_KEY);
// read key info
} catch (GSSException gsse) {
// deal with exception
}
}
```

GSSContext ctxt = m.createContext(...)
// Establishing the context
if (ctxt instanceof ExtendedGSSContext) {
ExtendedGSSContext ex = (ExtendedGSSContext)ctxt;
try {
Key key = (key)ex.inquireSecContext(
InquireType.KRB5_GET_SESSION_KEY);
// read key info
} catch (GSSException gsse) {
// deal with exception
}
}

requestDelegPolicy

```java
void requestDelegPolicy​(boolean state)
throws
GSSException
```

Requests that the delegation policy be respected. When a true value is
requested, the underlying context would use the delegation policy
defined by the environment as a hint to determine whether credentials
delegation should be performed. This request can only be made on the
context initiator's side and it has to be done prior to the first
call to

initSecContext

.

When this flag is false, delegation will only be tried when the

credentials delegation flag

is true.

When this flag is true but the

credentials delegation flag

is false, delegation will be only tried if the delegation policy permits
delegation.

When both this flag and the

credentials delegation flag

are true, delegation will be always tried. However, if the delegation
policy does not permit delegation, the value of

getDelegPolicyState()

will be false, even
if delegation is performed successfully.

In any case, if the delegation is not successful, the value returned
by

GSSContext.getCredDelegState()

is false, and the value
returned by

getDelegPolicyState()

is also false.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

**Parameters:** state

- true if the policy should be respected
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### requestDelegPolicy

void requestDelegPolicy​(boolean state)
throws

GSSException

Requests that the delegation policy be respected. When a true value is
requested, the underlying context would use the delegation policy
defined by the environment as a hint to determine whether credentials
delegation should be performed. This request can only be made on the
context initiator's side and it has to be done prior to the first
call to

initSecContext

.

When this flag is false, delegation will only be tried when the

credentials delegation flag

is true.

When this flag is true but the

credentials delegation flag

is false, delegation will be only tried if the delegation policy permits
delegation.

When both this flag and the

credentials delegation flag

are true, delegation will be always tried. However, if the delegation
policy does not permit delegation, the value of

getDelegPolicyState()

will be false, even
if delegation is performed successfully.

In any case, if the delegation is not successful, the value returned
by

GSSContext.getCredDelegState()

is false, and the value
returned by

getDelegPolicyState()

is also false.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

When this flag is false, delegation will only be tried when the

credentials delegation flag

is true.

When this flag is true but the

credentials delegation flag

is false, delegation will be only tried if the delegation policy permits
delegation.

When both this flag and the

credentials delegation flag

are true, delegation will be always tried. However, if the delegation
policy does not permit delegation, the value of

getDelegPolicyState()

will be false, even
if delegation is performed successfully.

In any case, if the delegation is not successful, the value returned
by

GSSContext.getCredDelegState()

is false, and the value
returned by

getDelegPolicyState()

is also false.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

When this flag is true but the

credentials delegation flag

is false, delegation will be only tried if the delegation policy permits
delegation.

When both this flag and the

credentials delegation flag

are true, delegation will be always tried. However, if the delegation
policy does not permit delegation, the value of

getDelegPolicyState()

will be false, even
if delegation is performed successfully.

In any case, if the delegation is not successful, the value returned
by

GSSContext.getCredDelegState()

is false, and the value
returned by

getDelegPolicyState()

is also false.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

When both this flag and the

credentials delegation flag

are true, delegation will be always tried. However, if the delegation
policy does not permit delegation, the value of

getDelegPolicyState()

will be false, even
if delegation is performed successfully.

In any case, if the delegation is not successful, the value returned
by

GSSContext.getCredDelegState()

is false, and the value
returned by

getDelegPolicyState()

is also false.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

In any case, if the delegation is not successful, the value returned
by

GSSContext.getCredDelegState()

is false, and the value
returned by

getDelegPolicyState()

is also false.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

Not all mechanisms support delegation policy. Therefore, the
application should check to see if the request was honored with the

getDelegPolicyState

method. When
delegation policy is not supported,

requestDelegPolicy

should return silently without throwing an exception.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

Note: for the Kerberos 5 mechanism, the delegation policy is expressed
through the OK-AS-DELEGATE flag in the service ticket. When it's true,
the KDC permits delegation to the target server. In a cross-realm
environment, in order for delegation be permitted, all cross-realm TGTs
on the authentication path must also have the OK-AS-DELAGATE flags set.

getDelegPolicyState

```java
boolean getDelegPolicyState()
```

Returns the delegation policy response. Called after a security context
is established. This method can be only called on the initiator's side.
See

requestDelegPolicy(boolean)

.

**Returns:** the delegation policy response

---

#### getDelegPolicyState

boolean getDelegPolicyState()

Returns the delegation policy response. Called after a security context
is established. This method can be only called on the initiator's side.
See

requestDelegPolicy(boolean)

.

---

