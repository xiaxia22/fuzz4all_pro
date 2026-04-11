# Interface Guard

**Source:** `java.base\java\security\Guard.html`

### Class Description

```java
public interface
Guard
```

This interface represents a guard, which is an object that is used
to protect access to another object.

This interface contains a single method,

checkGuard

,
with a single

object

argument.

checkGuard

is
invoked (by the GuardedObject

getObject

method)
to determine whether or not to allow access to the object.

**All Known Implementing Classes:** AllPermission

,

AttachPermission

,

AudioPermission

,

AuthPermission

,

AWTPermission

,

BasicPermission

,

CardPermission

,

DelegationPermission

,

FilePermission

,

FlightRecorderPermission

,

InquireSecContextPermission

,

JDIPermission

,

LinkPermission

,

LoggingPermission

,

ManagementPermission

,

MBeanPermission

,

MBeanServerPermission

,

MBeanTrustPermission

,

NetPermission

,

NetworkPermission

,

Permission

,

PrivateCredentialPermission

,

PropertyPermission

,

ReflectPermission

,

RuntimePermission

,

SecurityPermission

,

SerializablePermission

,

ServicePermission

,

SocketPermission

,

SQLPermission

,

SSLPermission

,

SubjectDelegationPermission

,

UnresolvedPermission

,

URLPermission

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void checkGuard​(
Object
object)
throws
SecurityException

Determines whether or not to allow access to the guarded object

object

. Returns silently if access is allowed.
Otherwise, throws a SecurityException.

**Parameters:**
- object

- the object being protected by the guard.

**Throws:**
- SecurityException

- if access is denied.

---

### Additional Sections

#### Interface Guard

**All Known Implementing Classes:** AllPermission

,

AttachPermission

,

AudioPermission

,

AuthPermission

,

AWTPermission

,

BasicPermission

,

CardPermission

,

DelegationPermission

,

FilePermission

,

FlightRecorderPermission

,

InquireSecContextPermission

,

JDIPermission

,

LinkPermission

,

LoggingPermission

,

ManagementPermission

,

MBeanPermission

,

MBeanServerPermission

,

MBeanTrustPermission

,

NetPermission

,

NetworkPermission

,

Permission

,

PrivateCredentialPermission

,

PropertyPermission

,

ReflectPermission

,

RuntimePermission

,

SecurityPermission

,

SerializablePermission

,

ServicePermission

,

SocketPermission

,

SQLPermission

,

SSLPermission

,

SubjectDelegationPermission

,

UnresolvedPermission

,

URLPermission

```java
public interface
Guard
```

This interface represents a guard, which is an object that is used
to protect access to another object.

This interface contains a single method,

checkGuard

,
with a single

object

argument.

checkGuard

is
invoked (by the GuardedObject

getObject

method)
to determine whether or not to allow access to the object.

**Since:** 1.2
**See Also:** GuardedObject

public interface

Guard

This interface represents a guard, which is an object that is used
to protect access to another object.

This interface contains a single method,

checkGuard

,
with a single

object

argument.

checkGuard

is
invoked (by the GuardedObject

getObject

method)
to determine whether or not to allow access to the object.

This interface contains a single method,

checkGuard

,
with a single

object

argument.

checkGuard

is
invoked (by the GuardedObject

getObject

method)
to determine whether or not to allow access to the object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

checkGuard

​(

Object

object)

Determines whether or not to allow access to the guarded object

object

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

checkGuard

​(

Object

object)

Determines whether or not to allow access to the guarded object

object

.

---

#### Method Summary

Determines whether or not to allow access to the guarded object

object

.

============ METHOD DETAIL ==========

- Method Detail

- checkGuard

```java
void checkGuard​(
Object
object)
throws
SecurityException
```

Determines whether or not to allow access to the guarded object

object

. Returns silently if access is allowed.
Otherwise, throws a SecurityException.

**Parameters:** object

- the object being protected by the guard.
**Throws:** SecurityException

- if access is denied.

Method Detail

- checkGuard

```java
void checkGuard​(
Object
object)
throws
SecurityException
```

Determines whether or not to allow access to the guarded object

object

. Returns silently if access is allowed.
Otherwise, throws a SecurityException.

**Parameters:** object

- the object being protected by the guard.
**Throws:** SecurityException

- if access is denied.

---

#### Method Detail

checkGuard

```java
void checkGuard​(
Object
object)
throws
SecurityException
```

Determines whether or not to allow access to the guarded object

object

. Returns silently if access is allowed.
Otherwise, throws a SecurityException.

**Parameters:** object

- the object being protected by the guard.
**Throws:** SecurityException

- if access is denied.

---

#### checkGuard

void checkGuard​(

Object

object)
throws

SecurityException

Determines whether or not to allow access to the guarded object

object

. Returns silently if access is allowed.
Otherwise, throws a SecurityException.

---

