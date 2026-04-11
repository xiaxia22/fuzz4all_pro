# Class SubjectDomainCombiner

**Source:** `java.base\javax\security\auth\SubjectDomainCombiner.html`

### Class Description

```java
public class
SubjectDomainCombiner

extends
Object

implements
DomainCombiner
```

A

SubjectDomainCombiner

updates ProtectionDomains
with Principals from the

Subject

associated with this

SubjectDomainCombiner

.

**All Implemented Interfaces:** DomainCombiner

---

### Field Details

*No entries found.*

### Constructor Details

#### public SubjectDomainCombiner​(
Subject
subject)

Associate the provided

Subject

with this

SubjectDomainCombiner

.

**Parameters:**
- subject

- the

Subject

to be associated with
with this

SubjectDomainCombiner

.

---

### Method Details

#### public
Subject
getSubject()

Get the

Subject

associated with this

SubjectDomainCombiner

.

**Returns:**
- the

Subject

associated with this

SubjectDomainCombiner

, or

null

if no

Subject

is associated with this

SubjectDomainCombiner

.

**Throws:**
- SecurityException

- if the caller does not have permission
to get the

Subject

associated with this

SubjectDomainCombiner

.

---

#### public
ProtectionDomain
[] combine​(
ProtectionDomain
[] currentDomains,

ProtectionDomain
[] assignedDomains)

Update the relevant ProtectionDomains with the Principals
from the

Subject

associated with this

SubjectDomainCombiner

.

A new

ProtectionDomain

instance is created
for each non-static

ProtectionDomain

(
(staticPermissionsOnly() == false)
in the

currentDomains

array. Each new

ProtectionDomain

instance is created using the

CodeSource

,

Permission

s and

ClassLoader

from the corresponding

ProtectionDomain

in

currentDomains

, as well as with the Principals from
the

Subject

associated with this

SubjectDomainCombiner

. Static ProtectionDomains are
combined as-is and no new instance is created.

All of the ProtectionDomains (static and newly instantiated) are
combined into a new array. The ProtectionDomains from the

assignedDomains

array are appended to this new array,
and the result is returned.

Note that optimizations such as the removal of duplicate
ProtectionDomains may have occurred.
In addition, caching of ProtectionDomains may be permitted.

**Specified by:**
- combine

in interface

DomainCombiner

**Parameters:**
- currentDomains

- the ProtectionDomains associated with the
current execution Thread, up to the most recent
privileged

ProtectionDomain

.
The ProtectionDomains are listed in order of execution,
with the most recently executing

ProtectionDomain

residing at the beginning of the array. This parameter may
be

null

if the current execution Thread
has no associated ProtectionDomains.
- assignedDomains

- the ProtectionDomains inherited from the
parent Thread, or the ProtectionDomains from the
privileged

context

, if a call to

AccessController.doPrivileged(..., context)

had occurred This parameter may be

null

if there were no ProtectionDomains inherited from the
parent Thread, or from the privileged

context

.

**Returns:**
- a new array consisting of the updated ProtectionDomains,
or

null

.

---

### Additional Sections

#### Class SubjectDomainCombiner

java.lang.Object

- javax.security.auth.SubjectDomainCombiner

javax.security.auth.SubjectDomainCombiner

**All Implemented Interfaces:** DomainCombiner

```java
public class
SubjectDomainCombiner

extends
Object

implements
DomainCombiner
```

A

SubjectDomainCombiner

updates ProtectionDomains
with Principals from the

Subject

associated with this

SubjectDomainCombiner

.

**Since:** 1.4

public class

SubjectDomainCombiner

extends

Object

implements

DomainCombiner

A

SubjectDomainCombiner

updates ProtectionDomains
with Principals from the

Subject

associated with this

SubjectDomainCombiner

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SubjectDomainCombiner

​(

Subject

subject)

Associate the provided

Subject

with this

SubjectDomainCombiner

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ProtectionDomain

[]

combine

​(

ProtectionDomain

[] currentDomains,

ProtectionDomain

[] assignedDomains)

Update the relevant ProtectionDomains with the Principals
from the

Subject

associated with this

SubjectDomainCombiner

.

Subject

getSubject

()

Get the

Subject

associated with this

SubjectDomainCombiner

.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

SubjectDomainCombiner

​(

Subject

subject)

Associate the provided

Subject

with this

SubjectDomainCombiner

.

---

#### Constructor Summary

Associate the provided

Subject

with this

SubjectDomainCombiner

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ProtectionDomain

[]

combine

​(

ProtectionDomain

[] currentDomains,

ProtectionDomain

[] assignedDomains)

Update the relevant ProtectionDomains with the Principals
from the

Subject

associated with this

SubjectDomainCombiner

.

Subject

getSubject

()

Get the

Subject

associated with this

SubjectDomainCombiner

.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Update the relevant ProtectionDomains with the Principals
from the

Subject

associated with this

SubjectDomainCombiner

.

Get the

Subject

associated with this

SubjectDomainCombiner

.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SubjectDomainCombiner

```java
public SubjectDomainCombiner​(
Subject
subject)
```

Associate the provided

Subject

with this

SubjectDomainCombiner

.

**Parameters:** subject

- the

Subject

to be associated with
with this

SubjectDomainCombiner

.

============ METHOD DETAIL ==========

- Method Detail

- getSubject

```java
public
Subject
getSubject()
```

Get the

Subject

associated with this

SubjectDomainCombiner

.

**Returns:** the

Subject

associated with this

SubjectDomainCombiner

, or

null

if no

Subject

is associated with this

SubjectDomainCombiner

.
**Throws:** SecurityException

- if the caller does not have permission
to get the

Subject

associated with this

SubjectDomainCombiner

.

- combine

```java
public
ProtectionDomain
[] combine​(
ProtectionDomain
[] currentDomains,

ProtectionDomain
[] assignedDomains)
```

Update the relevant ProtectionDomains with the Principals
from the

Subject

associated with this

SubjectDomainCombiner

.

A new

ProtectionDomain

instance is created
for each non-static

ProtectionDomain

(
(staticPermissionsOnly() == false)
in the

currentDomains

array. Each new

ProtectionDomain

instance is created using the

CodeSource

,

Permission

s and

ClassLoader

from the corresponding

ProtectionDomain

in

currentDomains

, as well as with the Principals from
the

Subject

associated with this

SubjectDomainCombiner

. Static ProtectionDomains are
combined as-is and no new instance is created.

All of the ProtectionDomains (static and newly instantiated) are
combined into a new array. The ProtectionDomains from the

assignedDomains

array are appended to this new array,
and the result is returned.

Note that optimizations such as the removal of duplicate
ProtectionDomains may have occurred.
In addition, caching of ProtectionDomains may be permitted.

**Specified by:** combine

in interface

DomainCombiner
**Parameters:** currentDomains

- the ProtectionDomains associated with the
current execution Thread, up to the most recent
privileged

ProtectionDomain

.
The ProtectionDomains are listed in order of execution,
with the most recently executing

ProtectionDomain

residing at the beginning of the array. This parameter may
be

null

if the current execution Thread
has no associated ProtectionDomains.
**Parameters:** assignedDomains

- the ProtectionDomains inherited from the
parent Thread, or the ProtectionDomains from the
privileged

context

, if a call to

AccessController.doPrivileged(..., context)

had occurred This parameter may be

null

if there were no ProtectionDomains inherited from the
parent Thread, or from the privileged

context

.
**Returns:** a new array consisting of the updated ProtectionDomains,
or

null

.

Constructor Detail

- SubjectDomainCombiner

```java
public SubjectDomainCombiner​(
Subject
subject)
```

Associate the provided

Subject

with this

SubjectDomainCombiner

.

**Parameters:** subject

- the

Subject

to be associated with
with this

SubjectDomainCombiner

.

---

#### Constructor Detail

SubjectDomainCombiner

```java
public SubjectDomainCombiner​(
Subject
subject)
```

Associate the provided

Subject

with this

SubjectDomainCombiner

.

**Parameters:** subject

- the

Subject

to be associated with
with this

SubjectDomainCombiner

.

---

#### SubjectDomainCombiner

public SubjectDomainCombiner​(

Subject

subject)

Associate the provided

Subject

with this

SubjectDomainCombiner

.

Method Detail

- getSubject

```java
public
Subject
getSubject()
```

Get the

Subject

associated with this

SubjectDomainCombiner

.

**Returns:** the

Subject

associated with this

SubjectDomainCombiner

, or

null

if no

Subject

is associated with this

SubjectDomainCombiner

.
**Throws:** SecurityException

- if the caller does not have permission
to get the

Subject

associated with this

SubjectDomainCombiner

.

- combine

```java
public
ProtectionDomain
[] combine​(
ProtectionDomain
[] currentDomains,

ProtectionDomain
[] assignedDomains)
```

Update the relevant ProtectionDomains with the Principals
from the

Subject

associated with this

SubjectDomainCombiner

.

A new

ProtectionDomain

instance is created
for each non-static

ProtectionDomain

(
(staticPermissionsOnly() == false)
in the

currentDomains

array. Each new

ProtectionDomain

instance is created using the

CodeSource

,

Permission

s and

ClassLoader

from the corresponding

ProtectionDomain

in

currentDomains

, as well as with the Principals from
the

Subject

associated with this

SubjectDomainCombiner

. Static ProtectionDomains are
combined as-is and no new instance is created.

All of the ProtectionDomains (static and newly instantiated) are
combined into a new array. The ProtectionDomains from the

assignedDomains

array are appended to this new array,
and the result is returned.

Note that optimizations such as the removal of duplicate
ProtectionDomains may have occurred.
In addition, caching of ProtectionDomains may be permitted.

**Specified by:** combine

in interface

DomainCombiner
**Parameters:** currentDomains

- the ProtectionDomains associated with the
current execution Thread, up to the most recent
privileged

ProtectionDomain

.
The ProtectionDomains are listed in order of execution,
with the most recently executing

ProtectionDomain

residing at the beginning of the array. This parameter may
be

null

if the current execution Thread
has no associated ProtectionDomains.
**Parameters:** assignedDomains

- the ProtectionDomains inherited from the
parent Thread, or the ProtectionDomains from the
privileged

context

, if a call to

AccessController.doPrivileged(..., context)

had occurred This parameter may be

null

if there were no ProtectionDomains inherited from the
parent Thread, or from the privileged

context

.
**Returns:** a new array consisting of the updated ProtectionDomains,
or

null

.

---

#### Method Detail

getSubject

```java
public
Subject
getSubject()
```

Get the

Subject

associated with this

SubjectDomainCombiner

.

**Returns:** the

Subject

associated with this

SubjectDomainCombiner

, or

null

if no

Subject

is associated with this

SubjectDomainCombiner

.
**Throws:** SecurityException

- if the caller does not have permission
to get the

Subject

associated with this

SubjectDomainCombiner

.

---

#### getSubject

public

Subject

getSubject()

Get the

Subject

associated with this

SubjectDomainCombiner

.

combine

```java
public
ProtectionDomain
[] combine​(
ProtectionDomain
[] currentDomains,

ProtectionDomain
[] assignedDomains)
```

Update the relevant ProtectionDomains with the Principals
from the

Subject

associated with this

SubjectDomainCombiner

.

A new

ProtectionDomain

instance is created
for each non-static

ProtectionDomain

(
(staticPermissionsOnly() == false)
in the

currentDomains

array. Each new

ProtectionDomain

instance is created using the

CodeSource

,

Permission

s and

ClassLoader

from the corresponding

ProtectionDomain

in

currentDomains

, as well as with the Principals from
the

Subject

associated with this

SubjectDomainCombiner

. Static ProtectionDomains are
combined as-is and no new instance is created.

All of the ProtectionDomains (static and newly instantiated) are
combined into a new array. The ProtectionDomains from the

assignedDomains

array are appended to this new array,
and the result is returned.

Note that optimizations such as the removal of duplicate
ProtectionDomains may have occurred.
In addition, caching of ProtectionDomains may be permitted.

**Specified by:** combine

in interface

DomainCombiner
**Parameters:** currentDomains

- the ProtectionDomains associated with the
current execution Thread, up to the most recent
privileged

ProtectionDomain

.
The ProtectionDomains are listed in order of execution,
with the most recently executing

ProtectionDomain

residing at the beginning of the array. This parameter may
be

null

if the current execution Thread
has no associated ProtectionDomains.
**Parameters:** assignedDomains

- the ProtectionDomains inherited from the
parent Thread, or the ProtectionDomains from the
privileged

context

, if a call to

AccessController.doPrivileged(..., context)

had occurred This parameter may be

null

if there were no ProtectionDomains inherited from the
parent Thread, or from the privileged

context

.
**Returns:** a new array consisting of the updated ProtectionDomains,
or

null

.

---

#### combine

public

ProtectionDomain

[] combine​(

ProtectionDomain

[] currentDomains,

ProtectionDomain

[] assignedDomains)

Update the relevant ProtectionDomains with the Principals
from the

Subject

associated with this

SubjectDomainCombiner

.

A new

ProtectionDomain

instance is created
for each non-static

ProtectionDomain

(
(staticPermissionsOnly() == false)
in the

currentDomains

array. Each new

ProtectionDomain

instance is created using the

CodeSource

,

Permission

s and

ClassLoader

from the corresponding

ProtectionDomain

in

currentDomains

, as well as with the Principals from
the

Subject

associated with this

SubjectDomainCombiner

. Static ProtectionDomains are
combined as-is and no new instance is created.

All of the ProtectionDomains (static and newly instantiated) are
combined into a new array. The ProtectionDomains from the

assignedDomains

array are appended to this new array,
and the result is returned.

Note that optimizations such as the removal of duplicate
ProtectionDomains may have occurred.
In addition, caching of ProtectionDomains may be permitted.

A new

ProtectionDomain

instance is created
for each non-static

ProtectionDomain

(
(staticPermissionsOnly() == false)
in the

currentDomains

array. Each new

ProtectionDomain

instance is created using the

CodeSource

,

Permission

s and

ClassLoader

from the corresponding

ProtectionDomain

in

currentDomains

, as well as with the Principals from
the

Subject

associated with this

SubjectDomainCombiner

. Static ProtectionDomains are
combined as-is and no new instance is created.

All of the ProtectionDomains (static and newly instantiated) are
combined into a new array. The ProtectionDomains from the

assignedDomains

array are appended to this new array,
and the result is returned.

Note that optimizations such as the removal of duplicate
ProtectionDomains may have occurred.
In addition, caching of ProtectionDomains may be permitted.

All of the ProtectionDomains (static and newly instantiated) are
combined into a new array. The ProtectionDomains from the

assignedDomains

array are appended to this new array,
and the result is returned.

Note that optimizations such as the removal of duplicate
ProtectionDomains may have occurred.
In addition, caching of ProtectionDomains may be permitted.

Note that optimizations such as the removal of duplicate
ProtectionDomains may have occurred.
In addition, caching of ProtectionDomains may be permitted.

---

