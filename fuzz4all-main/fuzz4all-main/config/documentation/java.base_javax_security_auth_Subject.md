# Class Subject

**Source:** `java.base\javax\security\auth\Subject.html`

### Class Description

```java
public final class
Subject

extends
Object

implements
Serializable
```

A

Subject

represents a grouping of related information
for a single entity, such as a person.
Such information includes the Subject's identities as well as
its security-related attributes
(passwords and cryptographic keys, for example).

Subjects may potentially have multiple identities.
Each identity is represented as a

Principal

within the

Subject

. Principals simply bind names to a

Subject

. For example, a

Subject

that happens
to be a person, Alice, might have two Principals:
one which binds "Alice Bar", the name on her driver license,
to the

Subject

, and another which binds,
"999-99-9999", the number on her student identification card,
to the

Subject

. Both Principals refer to the same

Subject

even though each has a different name.

A

Subject

may also own security-related attributes,
which are referred to as credentials.
Sensitive credentials that require special protection, such as
private cryptographic keys, are stored within a private credential

Set

. Credentials intended to be shared, such as
public key certificates or Kerberos server tickets are stored
within a public credential

Set

. Different permissions
are required to access and modify the different credential Sets.

To retrieve all the Principals associated with a

Subject

,
invoke the

getPrincipals

method. To retrieve
all the public or private credentials belonging to a

Subject

,
invoke the

getPublicCredentials

method or

getPrivateCredentials

method, respectively.
To modify the returned

Set

of Principals and credentials,
use the methods defined in the

Set

class.
For example:

```java
Subject subject;
Principal principal;
Object credential;

// add a Principal and credential to the Subject
subject.getPrincipals().add(principal);
subject.getPublicCredentials().add(credential);
```

This

Subject

class implements

Serializable

.
While the Principals associated with the

Subject

are serialized,
the credentials associated with the

Subject

are not.
Note that the

java.security.Principal

class
does not implement

Serializable

. Therefore all concrete

Principal

implementations associated with Subjects
must implement

Serializable

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Subject()

Create an instance of a

Subject

with an empty

Set

of Principals and empty
Sets of public and private credentials.

The newly constructed Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

---

#### public Subject​(boolean readOnly,

Set
<? extends
Principal
> principals,

Set
<?> pubCredentials,

Set
<?> privCredentials)

Create an instance of a

Subject

with
Principals and credentials.

The Principals and credentials from the specified Sets
are copied into newly constructed Sets.
These newly created Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

**Parameters:**
- readOnly

- true if the

Subject

is to be read-only,
and false otherwise.
- principals

- the

Set

of Principals
to be associated with this

Subject

.
- pubCredentials

- the

Set

of public credentials
to be associated with this

Subject

.
- privCredentials

- the

Set

of private credentials
to be associated with this

Subject

.

**Throws:**
- NullPointerException

- if the specified

principals

,

pubCredentials

,
or

privCredentials

are

null

,
or a null value exists within any of these three
Sets.

---

### Method Details

#### public void setReadOnly()

Set this

Subject

to be read-only.

Modifications (additions and removals) to this Subject's

Principal

Set

and
credential Sets will be disallowed.
The

destroy

operation on this Subject's credentials will
still be permitted.

Subsequent attempts to modify the Subject's

Principal

and credential Sets will result in an

IllegalStateException

being thrown.
Also, once a

Subject

is read-only,
it can not be reset to being writable again.

**Throws:**
- SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("setReadOnly")

permission to set this

Subject

to be read-only.

---

#### public boolean isReadOnly()

Query whether this

Subject

is read-only.

**Returns:**
- true if this

Subject

is read-only, false otherwise.

---

#### public static
Subject
getSubject​(
AccessControlContext
acc)

Get the

Subject

associated with the provided

AccessControlContext

.

The

AccessControlContext

may contain many
Subjects (from nested

doAs

calls).
In this situation, the most recent

Subject

associated
with the

AccessControlContext

is returned.

**Parameters:**
- acc

- the

AccessControlContext

from which to retrieve
the

Subject

.

**Returns:**
- the

Subject

associated with the provided

AccessControlContext

, or

null

if no

Subject

is associated
with the provided

AccessControlContext

.

**Throws:**
- SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("getSubject")

permission to get the

Subject

.
- NullPointerException

- if the provided

AccessControlContext

is

null

.

---

#### public static <T> T doAs​(
Subject
subject,

PrivilegedAction
<T> action)

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedAction

,
as well as the newly constructed

AccessControlContext

.

**Parameters:**
- subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
- action

- the code to be run as the specified

Subject

.

**Returns:**
- the value returned by the PrivilegedAction's

run

method.

**Throws:**
- NullPointerException

- if the

PrivilegedAction

is

null

.
- SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("doAs")

permission to invoke this
method.

**Type Parameters:**
- T

- the type of the value returned by the PrivilegedAction's

run

method.

---

#### public static <T> T doAs​(
Subject
subject,

PrivilegedExceptionAction
<T> action)
throws
PrivilegedActionException

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedExceptionAction

,
as well as the newly constructed

AccessControlContext

.

**Parameters:**
- subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
- action

- the code to be run as the specified

Subject

.

**Returns:**
- the value returned by the
PrivilegedExceptionAction's

run

method.

**Throws:**
- PrivilegedActionException

- if the

PrivilegedExceptionAction.run

method throws a checked exception.
- NullPointerException

- if the specified

PrivilegedExceptionAction

is

null

.
- SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("doAs")

permission to invoke this
method.

**Type Parameters:**
- T

- the type of the value returned by the
PrivilegedExceptionAction's

run

method.

---

#### public static <T> T doAsPrivileged​(
Subject
subject,

PrivilegedAction
<T> action,

AccessControlContext
acc)

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

**Parameters:**
- subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
- action

- the code to be run as the specified

Subject

.
- acc

- the

AccessControlContext

to be tied to the
specified

subject

and

action

.

**Returns:**
- the value returned by the PrivilegedAction's

run

method.

**Throws:**
- NullPointerException

- if the

PrivilegedAction

is

null

.
- SecurityException

- if a security manager is installed and the
caller does not have a

AuthPermission("doAsPrivileged")

permission to invoke
this method.

**Type Parameters:**
- T

- the type of the value returned by the PrivilegedAction's

run

method.

---

#### public static <T> T doAsPrivileged​(
Subject
subject,

PrivilegedExceptionAction
<T> action,

AccessControlContext
acc)
throws
PrivilegedActionException

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

**Parameters:**
- subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
- action

- the code to be run as the specified

Subject

.
- acc

- the

AccessControlContext

to be tied to the
specified

subject

and

action

.

**Returns:**
- the value returned by the
PrivilegedExceptionAction's

run

method.

**Throws:**
- PrivilegedActionException

- if the

PrivilegedExceptionAction.run

method throws a checked exception.
- NullPointerException

- if the specified

PrivilegedExceptionAction

is

null

.
- SecurityException

- if a security manager is installed and the
caller does not have a

AuthPermission("doAsPrivileged")

permission to invoke
this method.

**Type Parameters:**
- T

- the type of the value returned by the
PrivilegedExceptionAction's

run

method.

---

#### public
Set
<
Principal
> getPrincipals()

Return the

Set

of Principals associated with this

Subject

. Each

Principal

represents
an identity for this

Subject

.

The returned

Set

is backed by this Subject's
internal

Principal

Set

. Any modification
to the returned

Set

affects the internal

Principal

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrincipals")

permission to modify
the returned set, or a

SecurityException

will be thrown.

**Returns:**
- the

Set

of Principals associated with this

Subject

.

---

#### public <T extends
Principal
>
Set
<T> getPrincipals​(
Class
<T> c)

Return a

Set

of Principals associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal

Principal

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal

Principal

Set

.

**Parameters:**
- c

- the returned

Set

of Principals will all be
instances of this class.

**Returns:**
- a

Set

of Principals that are instances of the
specified

Class

.

**Throws:**
- NullPointerException

- if the specified

Class

is

null

.

**Type Parameters:**
- T

- the type of the class modeled by

c

---

#### public
Set
<
Object
> getPublicCredentials()

Return the

Set

of public credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal public Credential

Set

. Any modification
to the returned

Set

affects the internal public
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPublicCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

**Returns:**
- a

Set

of public credentials held by this

Subject

.

---

#### public
Set
<
Object
> getPrivateCredentials()

Return the

Set

of private credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal private Credential

Set

. Any modification
to the returned

Set

affects the internal private
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrivateCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

While iterating through the

Set

,
a

SecurityException

is thrown if a security manager is installed
and the caller does not have a

PrivateCredentialPermission

to access a particular Credential. The

Iterator

is nevertheless advanced to the next element in the

Set

.

**Returns:**
- a

Set

of private credentials held by this

Subject

.

---

#### public <T>
Set
<T> getPublicCredentials​(
Class
<T> c)

Return a

Set

of public credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal public Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal public Credential

Set

.

**Parameters:**
- c

- the returned

Set

of public credentials will all be
instances of this class.

**Returns:**
- a

Set

of public credentials that are instances
of the specified

Class

.

**Throws:**
- NullPointerException

- if the specified

Class

is

null

.

**Type Parameters:**
- T

- the type of the class modeled by

c

---

#### public <T>
Set
<T> getPrivateCredentials​(
Class
<T> c)

Return a

Set

of private credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

If a security manager is installed, the caller must have a

PrivateCredentialPermission

to access all of the requested
Credentials, or a

SecurityException

will be thrown.

The returned

Set

is not backed by this Subject's
internal private Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal private Credential

Set

.

**Parameters:**
- c

- the returned

Set

of private credentials will all be
instances of this class.

**Returns:**
- a

Set

of private credentials that are instances
of the specified

Class

.

**Throws:**
- NullPointerException

- if the specified

Class

is

null

.

**Type Parameters:**
- T

- the type of the class modeled by

c

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

Subject

for equality. Returns true if the given object is also a Subject
and the two

Subject

instances are equivalent.
More formally, two

Subject

instances are
equal if their

Principal

and

Credential

Sets are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- Object to be compared for equality with this

Subject

.

**Returns:**
- true if the specified Object is equal to this

Subject

.

**Throws:**
- SecurityException

- if a security manager is installed and the
caller does not have a

PrivateCredentialPermission

permission to access the private credentials for this

Subject

or the provided

Subject

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Return the String representation of this

Subject

.

**Overrides:**
- toString

in class

Object

**Returns:**
- the String representation of this

Subject

.

---

#### public int hashCode()

Returns a hashcode for this

Subject

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashcode for this

Subject

.

**Throws:**
- SecurityException

- if a security manager is installed and the
caller does not have a

PrivateCredentialPermission

permission to access this Subject's private credentials.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class Subject

java.lang.Object

- javax.security.auth.Subject

javax.security.auth.Subject

**All Implemented Interfaces:** Serializable

```java
public final class
Subject

extends
Object

implements
Serializable
```

A

Subject

represents a grouping of related information
for a single entity, such as a person.
Such information includes the Subject's identities as well as
its security-related attributes
(passwords and cryptographic keys, for example).

Subjects may potentially have multiple identities.
Each identity is represented as a

Principal

within the

Subject

. Principals simply bind names to a

Subject

. For example, a

Subject

that happens
to be a person, Alice, might have two Principals:
one which binds "Alice Bar", the name on her driver license,
to the

Subject

, and another which binds,
"999-99-9999", the number on her student identification card,
to the

Subject

. Both Principals refer to the same

Subject

even though each has a different name.

A

Subject

may also own security-related attributes,
which are referred to as credentials.
Sensitive credentials that require special protection, such as
private cryptographic keys, are stored within a private credential

Set

. Credentials intended to be shared, such as
public key certificates or Kerberos server tickets are stored
within a public credential

Set

. Different permissions
are required to access and modify the different credential Sets.

To retrieve all the Principals associated with a

Subject

,
invoke the

getPrincipals

method. To retrieve
all the public or private credentials belonging to a

Subject

,
invoke the

getPublicCredentials

method or

getPrivateCredentials

method, respectively.
To modify the returned

Set

of Principals and credentials,
use the methods defined in the

Set

class.
For example:

```java
Subject subject;
Principal principal;
Object credential;

// add a Principal and credential to the Subject
subject.getPrincipals().add(principal);
subject.getPublicCredentials().add(credential);
```

This

Subject

class implements

Serializable

.
While the Principals associated with the

Subject

are serialized,
the credentials associated with the

Subject

are not.
Note that the

java.security.Principal

class
does not implement

Serializable

. Therefore all concrete

Principal

implementations associated with Subjects
must implement

Serializable

.

**Since:** 1.4
**See Also:** Principal

,

DomainCombiner

,

Serialized Form

public final class

Subject

extends

Object

implements

Serializable

A

Subject

represents a grouping of related information
for a single entity, such as a person.
Such information includes the Subject's identities as well as
its security-related attributes
(passwords and cryptographic keys, for example).

Subjects may potentially have multiple identities.
Each identity is represented as a

Principal

within the

Subject

. Principals simply bind names to a

Subject

. For example, a

Subject

that happens
to be a person, Alice, might have two Principals:
one which binds "Alice Bar", the name on her driver license,
to the

Subject

, and another which binds,
"999-99-9999", the number on her student identification card,
to the

Subject

. Both Principals refer to the same

Subject

even though each has a different name.

A

Subject

may also own security-related attributes,
which are referred to as credentials.
Sensitive credentials that require special protection, such as
private cryptographic keys, are stored within a private credential

Set

. Credentials intended to be shared, such as
public key certificates or Kerberos server tickets are stored
within a public credential

Set

. Different permissions
are required to access and modify the different credential Sets.

To retrieve all the Principals associated with a

Subject

,
invoke the

getPrincipals

method. To retrieve
all the public or private credentials belonging to a

Subject

,
invoke the

getPublicCredentials

method or

getPrivateCredentials

method, respectively.
To modify the returned

Set

of Principals and credentials,
use the methods defined in the

Set

class.
For example:

```java
Subject subject;
Principal principal;
Object credential;

// add a Principal and credential to the Subject
subject.getPrincipals().add(principal);
subject.getPublicCredentials().add(credential);
```

This

Subject

class implements

Serializable

.
While the Principals associated with the

Subject

are serialized,
the credentials associated with the

Subject

are not.
Note that the

java.security.Principal

class
does not implement

Serializable

. Therefore all concrete

Principal

implementations associated with Subjects
must implement

Serializable

.

Subjects may potentially have multiple identities.
Each identity is represented as a

Principal

within the

Subject

. Principals simply bind names to a

Subject

. For example, a

Subject

that happens
to be a person, Alice, might have two Principals:
one which binds "Alice Bar", the name on her driver license,
to the

Subject

, and another which binds,
"999-99-9999", the number on her student identification card,
to the

Subject

. Both Principals refer to the same

Subject

even though each has a different name.

A

Subject

may also own security-related attributes,
which are referred to as credentials.
Sensitive credentials that require special protection, such as
private cryptographic keys, are stored within a private credential

Set

. Credentials intended to be shared, such as
public key certificates or Kerberos server tickets are stored
within a public credential

Set

. Different permissions
are required to access and modify the different credential Sets.

To retrieve all the Principals associated with a

Subject

,
invoke the

getPrincipals

method. To retrieve
all the public or private credentials belonging to a

Subject

,
invoke the

getPublicCredentials

method or

getPrivateCredentials

method, respectively.
To modify the returned

Set

of Principals and credentials,
use the methods defined in the

Set

class.
For example:

```java
Subject subject;
Principal principal;
Object credential;

// add a Principal and credential to the Subject
subject.getPrincipals().add(principal);
subject.getPublicCredentials().add(credential);
```

This

Subject

class implements

Serializable

.
While the Principals associated with the

Subject

are serialized,
the credentials associated with the

Subject

are not.
Note that the

java.security.Principal

class
does not implement

Serializable

. Therefore all concrete

Principal

implementations associated with Subjects
must implement

Serializable

.

A

Subject

may also own security-related attributes,
which are referred to as credentials.
Sensitive credentials that require special protection, such as
private cryptographic keys, are stored within a private credential

Set

. Credentials intended to be shared, such as
public key certificates or Kerberos server tickets are stored
within a public credential

Set

. Different permissions
are required to access and modify the different credential Sets.

To retrieve all the Principals associated with a

Subject

,
invoke the

getPrincipals

method. To retrieve
all the public or private credentials belonging to a

Subject

,
invoke the

getPublicCredentials

method or

getPrivateCredentials

method, respectively.
To modify the returned

Set

of Principals and credentials,
use the methods defined in the

Set

class.
For example:

```java
Subject subject;
Principal principal;
Object credential;

// add a Principal and credential to the Subject
subject.getPrincipals().add(principal);
subject.getPublicCredentials().add(credential);
```

This

Subject

class implements

Serializable

.
While the Principals associated with the

Subject

are serialized,
the credentials associated with the

Subject

are not.
Note that the

java.security.Principal

class
does not implement

Serializable

. Therefore all concrete

Principal

implementations associated with Subjects
must implement

Serializable

.

To retrieve all the Principals associated with a

Subject

,
invoke the

getPrincipals

method. To retrieve
all the public or private credentials belonging to a

Subject

,
invoke the

getPublicCredentials

method or

getPrivateCredentials

method, respectively.
To modify the returned

Set

of Principals and credentials,
use the methods defined in the

Set

class.
For example:

```java
Subject subject;
Principal principal;
Object credential;

// add a Principal and credential to the Subject
subject.getPrincipals().add(principal);
subject.getPublicCredentials().add(credential);
```

This

Subject

class implements

Serializable

.
While the Principals associated with the

Subject

are serialized,
the credentials associated with the

Subject

are not.
Note that the

java.security.Principal

class
does not implement

Serializable

. Therefore all concrete

Principal

implementations associated with Subjects
must implement

Serializable

.

Subject subject;
Principal principal;
Object credential;

// add a Principal and credential to the Subject
subject.getPrincipals().add(principal);
subject.getPublicCredentials().add(credential);

This

Subject

class implements

Serializable

.
While the Principals associated with the

Subject

are serialized,
the credentials associated with the

Subject

are not.
Note that the

java.security.Principal

class
does not implement

Serializable

. Therefore all concrete

Principal

implementations associated with Subjects
must implement

Serializable

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Subject

()

Create an instance of a

Subject

with an empty

Set

of Principals and empty
Sets of public and private credentials.

Subject

​(boolean readOnly,

Set

<? extends

Principal

> principals,

Set

<?> pubCredentials,

Set

<?> privCredentials)

Create an instance of a

Subject

with
Principals and credentials.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static <T> T

doAs

​(

Subject

subject,

PrivilegedAction

<T> action)

Perform work as a particular

Subject

.

static <T> T

doAs

​(

Subject

subject,

PrivilegedExceptionAction

<T> action)

Perform work as a particular

Subject

.

static <T> T

doAsPrivileged

​(

Subject

subject,

PrivilegedAction

<T> action,

AccessControlContext

acc)

Perform privileged work as a particular

Subject

.

static <T> T

doAsPrivileged

​(

Subject

subject,

PrivilegedExceptionAction

<T> action,

AccessControlContext

acc)

Perform privileged work as a particular

Subject

.

boolean

equals

​(

Object

o)

Compares the specified Object with this

Subject

for equality.

Set

<

Principal

>

getPrincipals

()

Return the

Set

of Principals associated with this

Subject

.

<T extends

Principal

>

Set

<T>

getPrincipals

​(

Class

<T> c)

Return a

Set

of Principals associated with this

Subject

that are instances or subclasses of the specified

Class

.

Set

<

Object

>

getPrivateCredentials

()

Return the

Set

of private credentials held by this

Subject

.

<T>

Set

<T>

getPrivateCredentials

​(

Class

<T> c)

Return a

Set

of private credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

Set

<

Object

>

getPublicCredentials

()

Return the

Set

of public credentials held by this

Subject

.

<T>

Set

<T>

getPublicCredentials

​(

Class

<T> c)

Return a

Set

of public credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

static

Subject

getSubject

​(

AccessControlContext

acc)

Get the

Subject

associated with the provided

AccessControlContext

.

int

hashCode

()

Returns a hashcode for this

Subject

.

boolean

isReadOnly

()

Query whether this

Subject

is read-only.

void

setReadOnly

()

Set this

Subject

to be read-only.

String

toString

()

Return the String representation of this

Subject

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

Subject

()

Create an instance of a

Subject

with an empty

Set

of Principals and empty
Sets of public and private credentials.

Subject

​(boolean readOnly,

Set

<? extends

Principal

> principals,

Set

<?> pubCredentials,

Set

<?> privCredentials)

Create an instance of a

Subject

with
Principals and credentials.

---

#### Constructor Summary

Create an instance of a

Subject

with an empty

Set

of Principals and empty
Sets of public and private credentials.

Create an instance of a

Subject

with
Principals and credentials.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static <T> T

doAs

​(

Subject

subject,

PrivilegedAction

<T> action)

Perform work as a particular

Subject

.

static <T> T

doAs

​(

Subject

subject,

PrivilegedExceptionAction

<T> action)

Perform work as a particular

Subject

.

static <T> T

doAsPrivileged

​(

Subject

subject,

PrivilegedAction

<T> action,

AccessControlContext

acc)

Perform privileged work as a particular

Subject

.

static <T> T

doAsPrivileged

​(

Subject

subject,

PrivilegedExceptionAction

<T> action,

AccessControlContext

acc)

Perform privileged work as a particular

Subject

.

boolean

equals

​(

Object

o)

Compares the specified Object with this

Subject

for equality.

Set

<

Principal

>

getPrincipals

()

Return the

Set

of Principals associated with this

Subject

.

<T extends

Principal

>

Set

<T>

getPrincipals

​(

Class

<T> c)

Return a

Set

of Principals associated with this

Subject

that are instances or subclasses of the specified

Class

.

Set

<

Object

>

getPrivateCredentials

()

Return the

Set

of private credentials held by this

Subject

.

<T>

Set

<T>

getPrivateCredentials

​(

Class

<T> c)

Return a

Set

of private credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

Set

<

Object

>

getPublicCredentials

()

Return the

Set

of public credentials held by this

Subject

.

<T>

Set

<T>

getPublicCredentials

​(

Class

<T> c)

Return a

Set

of public credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

static

Subject

getSubject

​(

AccessControlContext

acc)

Get the

Subject

associated with the provided

AccessControlContext

.

int

hashCode

()

Returns a hashcode for this

Subject

.

boolean

isReadOnly

()

Query whether this

Subject

is read-only.

void

setReadOnly

()

Set this

Subject

to be read-only.

String

toString

()

Return the String representation of this

Subject

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Perform work as a particular

Subject

.

Perform privileged work as a particular

Subject

.

Compares the specified Object with this

Subject

for equality.

Return the

Set

of Principals associated with this

Subject

.

Return a

Set

of Principals associated with this

Subject

that are instances or subclasses of the specified

Class

.

Return the

Set

of private credentials held by this

Subject

.

Return a

Set

of private credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

Return the

Set

of public credentials held by this

Subject

.

Return a

Set

of public credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

Get the

Subject

associated with the provided

AccessControlContext

.

Returns a hashcode for this

Subject

.

Query whether this

Subject

is read-only.

Set this

Subject

to be read-only.

Return the String representation of this

Subject

.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- Subject

```java
public Subject()
```

Create an instance of a

Subject

with an empty

Set

of Principals and empty
Sets of public and private credentials.

The newly constructed Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

- Subject

```java
public Subject​(boolean readOnly,

Set
<? extends
Principal
> principals,

Set
<?> pubCredentials,

Set
<?> privCredentials)
```

Create an instance of a

Subject

with
Principals and credentials.

The Principals and credentials from the specified Sets
are copied into newly constructed Sets.
These newly created Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

**Parameters:** readOnly

- true if the

Subject

is to be read-only,
and false otherwise.
**Parameters:** principals

- the

Set

of Principals
to be associated with this

Subject

.
**Parameters:** pubCredentials

- the

Set

of public credentials
to be associated with this

Subject

.
**Parameters:** privCredentials

- the

Set

of private credentials
to be associated with this

Subject

.
**Throws:** NullPointerException

- if the specified

principals

,

pubCredentials

,
or

privCredentials

are

null

,
or a null value exists within any of these three
Sets.

============ METHOD DETAIL ==========

- Method Detail

- setReadOnly

```java
public void setReadOnly()
```

Set this

Subject

to be read-only.

Modifications (additions and removals) to this Subject's

Principal

Set

and
credential Sets will be disallowed.
The

destroy

operation on this Subject's credentials will
still be permitted.

Subsequent attempts to modify the Subject's

Principal

and credential Sets will result in an

IllegalStateException

being thrown.
Also, once a

Subject

is read-only,
it can not be reset to being writable again.

**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("setReadOnly")

permission to set this

Subject

to be read-only.

- isReadOnly

```java
public boolean isReadOnly()
```

Query whether this

Subject

is read-only.

**Returns:** true if this

Subject

is read-only, false otherwise.

- getSubject

```java
public static
Subject
getSubject​(
AccessControlContext
acc)
```

Get the

Subject

associated with the provided

AccessControlContext

.

The

AccessControlContext

may contain many
Subjects (from nested

doAs

calls).
In this situation, the most recent

Subject

associated
with the

AccessControlContext

is returned.

**Parameters:** acc

- the

AccessControlContext

from which to retrieve
the

Subject

.
**Returns:** the

Subject

associated with the provided

AccessControlContext

, or

null

if no

Subject

is associated
with the provided

AccessControlContext

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("getSubject")

permission to get the

Subject

.
**Throws:** NullPointerException

- if the provided

AccessControlContext

is

null

.

- doAs

```java
public static <T> T doAs​(
Subject
subject,

PrivilegedAction
<T> action)
```

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedAction

,
as well as the newly constructed

AccessControlContext

.

**Type Parameters:** T

- the type of the value returned by the PrivilegedAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Returns:** the value returned by the PrivilegedAction's

run

method.
**Throws:** NullPointerException

- if the

PrivilegedAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("doAs")

permission to invoke this
method.

- doAs

```java
public static <T> T doAs​(
Subject
subject,

PrivilegedExceptionAction
<T> action)
throws
PrivilegedActionException
```

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedExceptionAction

,
as well as the newly constructed

AccessControlContext

.

**Type Parameters:** T

- the type of the value returned by the
PrivilegedExceptionAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Returns:** the value returned by the
PrivilegedExceptionAction's

run

method.
**Throws:** PrivilegedActionException

- if the

PrivilegedExceptionAction.run

method throws a checked exception.
**Throws:** NullPointerException

- if the specified

PrivilegedExceptionAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("doAs")

permission to invoke this
method.

- doAsPrivileged

```java
public static <T> T doAsPrivileged​(
Subject
subject,

PrivilegedAction
<T> action,

AccessControlContext
acc)
```

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

**Type Parameters:** T

- the type of the value returned by the PrivilegedAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Parameters:** acc

- the

AccessControlContext

to be tied to the
specified

subject

and

action

.
**Returns:** the value returned by the PrivilegedAction's

run

method.
**Throws:** NullPointerException

- if the

PrivilegedAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

AuthPermission("doAsPrivileged")

permission to invoke
this method.

- doAsPrivileged

```java
public static <T> T doAsPrivileged​(
Subject
subject,

PrivilegedExceptionAction
<T> action,

AccessControlContext
acc)
throws
PrivilegedActionException
```

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

**Type Parameters:** T

- the type of the value returned by the
PrivilegedExceptionAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Parameters:** acc

- the

AccessControlContext

to be tied to the
specified

subject

and

action

.
**Returns:** the value returned by the
PrivilegedExceptionAction's

run

method.
**Throws:** PrivilegedActionException

- if the

PrivilegedExceptionAction.run

method throws a checked exception.
**Throws:** NullPointerException

- if the specified

PrivilegedExceptionAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

AuthPermission("doAsPrivileged")

permission to invoke
this method.

- getPrincipals

```java
public
Set
<
Principal
> getPrincipals()
```

Return the

Set

of Principals associated with this

Subject

. Each

Principal

represents
an identity for this

Subject

.

The returned

Set

is backed by this Subject's
internal

Principal

Set

. Any modification
to the returned

Set

affects the internal

Principal

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrincipals")

permission to modify
the returned set, or a

SecurityException

will be thrown.

**Returns:** the

Set

of Principals associated with this

Subject

.

- getPrincipals

```java
public <T extends
Principal
>
Set
<T> getPrincipals​(
Class
<T> c)
```

Return a

Set

of Principals associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal

Principal

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal

Principal

Set

.

**Type Parameters:** T

- the type of the class modeled by

c
**Parameters:** c

- the returned

Set

of Principals will all be
instances of this class.
**Returns:** a

Set

of Principals that are instances of the
specified

Class

.
**Throws:** NullPointerException

- if the specified

Class

is

null

.

- getPublicCredentials

```java
public
Set
<
Object
> getPublicCredentials()
```

Return the

Set

of public credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal public Credential

Set

. Any modification
to the returned

Set

affects the internal public
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPublicCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

**Returns:** a

Set

of public credentials held by this

Subject

.

- getPrivateCredentials

```java
public
Set
<
Object
> getPrivateCredentials()
```

Return the

Set

of private credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal private Credential

Set

. Any modification
to the returned

Set

affects the internal private
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrivateCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

While iterating through the

Set

,
a

SecurityException

is thrown if a security manager is installed
and the caller does not have a

PrivateCredentialPermission

to access a particular Credential. The

Iterator

is nevertheless advanced to the next element in the

Set

.

**Returns:** a

Set

of private credentials held by this

Subject

.

- getPublicCredentials

```java
public <T>
Set
<T> getPublicCredentials​(
Class
<T> c)
```

Return a

Set

of public credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal public Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal public Credential

Set

.

**Type Parameters:** T

- the type of the class modeled by

c
**Parameters:** c

- the returned

Set

of public credentials will all be
instances of this class.
**Returns:** a

Set

of public credentials that are instances
of the specified

Class

.
**Throws:** NullPointerException

- if the specified

Class

is

null

.

- getPrivateCredentials

```java
public <T>
Set
<T> getPrivateCredentials​(
Class
<T> c)
```

Return a

Set

of private credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

If a security manager is installed, the caller must have a

PrivateCredentialPermission

to access all of the requested
Credentials, or a

SecurityException

will be thrown.

The returned

Set

is not backed by this Subject's
internal private Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal private Credential

Set

.

**Type Parameters:** T

- the type of the class modeled by

c
**Parameters:** c

- the returned

Set

of private credentials will all be
instances of this class.
**Returns:** a

Set

of private credentials that are instances
of the specified

Class

.
**Throws:** NullPointerException

- if the specified

Class

is

null

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

Subject

for equality. Returns true if the given object is also a Subject
and the two

Subject

instances are equivalent.
More formally, two

Subject

instances are
equal if their

Principal

and

Credential

Sets are equal.

**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

Subject

.
**Returns:** true if the specified Object is equal to this

Subject

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

PrivateCredentialPermission

permission to access the private credentials for this

Subject

or the provided

Subject

.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Return the String representation of this

Subject

.

**Overrides:** toString

in class

Object
**Returns:** the String representation of this

Subject

.

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this

Subject

.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode for this

Subject

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

PrivateCredentialPermission

permission to access this Subject's private credentials.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- Subject

```java
public Subject()
```

Create an instance of a

Subject

with an empty

Set

of Principals and empty
Sets of public and private credentials.

The newly constructed Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

- Subject

```java
public Subject​(boolean readOnly,

Set
<? extends
Principal
> principals,

Set
<?> pubCredentials,

Set
<?> privCredentials)
```

Create an instance of a

Subject

with
Principals and credentials.

The Principals and credentials from the specified Sets
are copied into newly constructed Sets.
These newly created Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

**Parameters:** readOnly

- true if the

Subject

is to be read-only,
and false otherwise.
**Parameters:** principals

- the

Set

of Principals
to be associated with this

Subject

.
**Parameters:** pubCredentials

- the

Set

of public credentials
to be associated with this

Subject

.
**Parameters:** privCredentials

- the

Set

of private credentials
to be associated with this

Subject

.
**Throws:** NullPointerException

- if the specified

principals

,

pubCredentials

,
or

privCredentials

are

null

,
or a null value exists within any of these three
Sets.

---

#### Constructor Detail

Subject

```java
public Subject()
```

Create an instance of a

Subject

with an empty

Set

of Principals and empty
Sets of public and private credentials.

The newly constructed Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

---

#### Subject

public Subject()

Create an instance of a

Subject

with an empty

Set

of Principals and empty
Sets of public and private credentials.

The newly constructed Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

The newly constructed Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

Subject

```java
public Subject​(boolean readOnly,

Set
<? extends
Principal
> principals,

Set
<?> pubCredentials,

Set
<?> privCredentials)
```

Create an instance of a

Subject

with
Principals and credentials.

The Principals and credentials from the specified Sets
are copied into newly constructed Sets.
These newly created Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

**Parameters:** readOnly

- true if the

Subject

is to be read-only,
and false otherwise.
**Parameters:** principals

- the

Set

of Principals
to be associated with this

Subject

.
**Parameters:** pubCredentials

- the

Set

of public credentials
to be associated with this

Subject

.
**Parameters:** privCredentials

- the

Set

of private credentials
to be associated with this

Subject

.
**Throws:** NullPointerException

- if the specified

principals

,

pubCredentials

,
or

privCredentials

are

null

,
or a null value exists within any of these three
Sets.

---

#### Subject

public Subject​(boolean readOnly,

Set

<? extends

Principal

> principals,

Set

<?> pubCredentials,

Set

<?> privCredentials)

Create an instance of a

Subject

with
Principals and credentials.

The Principals and credentials from the specified Sets
are copied into newly constructed Sets.
These newly created Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

The Principals and credentials from the specified Sets
are copied into newly constructed Sets.
These newly created Sets check whether this

Subject

has been set read-only before permitting subsequent modifications.
The newly created Sets also prevent illegal modifications
by ensuring that callers have sufficient permissions. These Sets
also prohibit null elements, and attempts to add or query a null
element will result in a

NullPointerException

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

To modify the Principals Set, the caller must have

AuthPermission("modifyPrincipals")

.
To modify the public credential Set, the caller must have

AuthPermission("modifyPublicCredentials")

.
To modify the private credential Set, the caller must have

AuthPermission("modifyPrivateCredentials")

.

Method Detail

- setReadOnly

```java
public void setReadOnly()
```

Set this

Subject

to be read-only.

Modifications (additions and removals) to this Subject's

Principal

Set

and
credential Sets will be disallowed.
The

destroy

operation on this Subject's credentials will
still be permitted.

Subsequent attempts to modify the Subject's

Principal

and credential Sets will result in an

IllegalStateException

being thrown.
Also, once a

Subject

is read-only,
it can not be reset to being writable again.

**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("setReadOnly")

permission to set this

Subject

to be read-only.

- isReadOnly

```java
public boolean isReadOnly()
```

Query whether this

Subject

is read-only.

**Returns:** true if this

Subject

is read-only, false otherwise.

- getSubject

```java
public static
Subject
getSubject​(
AccessControlContext
acc)
```

Get the

Subject

associated with the provided

AccessControlContext

.

The

AccessControlContext

may contain many
Subjects (from nested

doAs

calls).
In this situation, the most recent

Subject

associated
with the

AccessControlContext

is returned.

**Parameters:** acc

- the

AccessControlContext

from which to retrieve
the

Subject

.
**Returns:** the

Subject

associated with the provided

AccessControlContext

, or

null

if no

Subject

is associated
with the provided

AccessControlContext

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("getSubject")

permission to get the

Subject

.
**Throws:** NullPointerException

- if the provided

AccessControlContext

is

null

.

- doAs

```java
public static <T> T doAs​(
Subject
subject,

PrivilegedAction
<T> action)
```

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedAction

,
as well as the newly constructed

AccessControlContext

.

**Type Parameters:** T

- the type of the value returned by the PrivilegedAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Returns:** the value returned by the PrivilegedAction's

run

method.
**Throws:** NullPointerException

- if the

PrivilegedAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("doAs")

permission to invoke this
method.

- doAs

```java
public static <T> T doAs​(
Subject
subject,

PrivilegedExceptionAction
<T> action)
throws
PrivilegedActionException
```

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedExceptionAction

,
as well as the newly constructed

AccessControlContext

.

**Type Parameters:** T

- the type of the value returned by the
PrivilegedExceptionAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Returns:** the value returned by the
PrivilegedExceptionAction's

run

method.
**Throws:** PrivilegedActionException

- if the

PrivilegedExceptionAction.run

method throws a checked exception.
**Throws:** NullPointerException

- if the specified

PrivilegedExceptionAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("doAs")

permission to invoke this
method.

- doAsPrivileged

```java
public static <T> T doAsPrivileged​(
Subject
subject,

PrivilegedAction
<T> action,

AccessControlContext
acc)
```

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

**Type Parameters:** T

- the type of the value returned by the PrivilegedAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Parameters:** acc

- the

AccessControlContext

to be tied to the
specified

subject

and

action

.
**Returns:** the value returned by the PrivilegedAction's

run

method.
**Throws:** NullPointerException

- if the

PrivilegedAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

AuthPermission("doAsPrivileged")

permission to invoke
this method.

- doAsPrivileged

```java
public static <T> T doAsPrivileged​(
Subject
subject,

PrivilegedExceptionAction
<T> action,

AccessControlContext
acc)
throws
PrivilegedActionException
```

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

**Type Parameters:** T

- the type of the value returned by the
PrivilegedExceptionAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Parameters:** acc

- the

AccessControlContext

to be tied to the
specified

subject

and

action

.
**Returns:** the value returned by the
PrivilegedExceptionAction's

run

method.
**Throws:** PrivilegedActionException

- if the

PrivilegedExceptionAction.run

method throws a checked exception.
**Throws:** NullPointerException

- if the specified

PrivilegedExceptionAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

AuthPermission("doAsPrivileged")

permission to invoke
this method.

- getPrincipals

```java
public
Set
<
Principal
> getPrincipals()
```

Return the

Set

of Principals associated with this

Subject

. Each

Principal

represents
an identity for this

Subject

.

The returned

Set

is backed by this Subject's
internal

Principal

Set

. Any modification
to the returned

Set

affects the internal

Principal

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrincipals")

permission to modify
the returned set, or a

SecurityException

will be thrown.

**Returns:** the

Set

of Principals associated with this

Subject

.

- getPrincipals

```java
public <T extends
Principal
>
Set
<T> getPrincipals​(
Class
<T> c)
```

Return a

Set

of Principals associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal

Principal

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal

Principal

Set

.

**Type Parameters:** T

- the type of the class modeled by

c
**Parameters:** c

- the returned

Set

of Principals will all be
instances of this class.
**Returns:** a

Set

of Principals that are instances of the
specified

Class

.
**Throws:** NullPointerException

- if the specified

Class

is

null

.

- getPublicCredentials

```java
public
Set
<
Object
> getPublicCredentials()
```

Return the

Set

of public credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal public Credential

Set

. Any modification
to the returned

Set

affects the internal public
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPublicCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

**Returns:** a

Set

of public credentials held by this

Subject

.

- getPrivateCredentials

```java
public
Set
<
Object
> getPrivateCredentials()
```

Return the

Set

of private credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal private Credential

Set

. Any modification
to the returned

Set

affects the internal private
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrivateCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

While iterating through the

Set

,
a

SecurityException

is thrown if a security manager is installed
and the caller does not have a

PrivateCredentialPermission

to access a particular Credential. The

Iterator

is nevertheless advanced to the next element in the

Set

.

**Returns:** a

Set

of private credentials held by this

Subject

.

- getPublicCredentials

```java
public <T>
Set
<T> getPublicCredentials​(
Class
<T> c)
```

Return a

Set

of public credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal public Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal public Credential

Set

.

**Type Parameters:** T

- the type of the class modeled by

c
**Parameters:** c

- the returned

Set

of public credentials will all be
instances of this class.
**Returns:** a

Set

of public credentials that are instances
of the specified

Class

.
**Throws:** NullPointerException

- if the specified

Class

is

null

.

- getPrivateCredentials

```java
public <T>
Set
<T> getPrivateCredentials​(
Class
<T> c)
```

Return a

Set

of private credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

If a security manager is installed, the caller must have a

PrivateCredentialPermission

to access all of the requested
Credentials, or a

SecurityException

will be thrown.

The returned

Set

is not backed by this Subject's
internal private Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal private Credential

Set

.

**Type Parameters:** T

- the type of the class modeled by

c
**Parameters:** c

- the returned

Set

of private credentials will all be
instances of this class.
**Returns:** a

Set

of private credentials that are instances
of the specified

Class

.
**Throws:** NullPointerException

- if the specified

Class

is

null

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

Subject

for equality. Returns true if the given object is also a Subject
and the two

Subject

instances are equivalent.
More formally, two

Subject

instances are
equal if their

Principal

and

Credential

Sets are equal.

**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

Subject

.
**Returns:** true if the specified Object is equal to this

Subject

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

PrivateCredentialPermission

permission to access the private credentials for this

Subject

or the provided

Subject

.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Return the String representation of this

Subject

.

**Overrides:** toString

in class

Object
**Returns:** the String representation of this

Subject

.

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this

Subject

.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode for this

Subject

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

PrivateCredentialPermission

permission to access this Subject's private credentials.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

setReadOnly

```java
public void setReadOnly()
```

Set this

Subject

to be read-only.

Modifications (additions and removals) to this Subject's

Principal

Set

and
credential Sets will be disallowed.
The

destroy

operation on this Subject's credentials will
still be permitted.

Subsequent attempts to modify the Subject's

Principal

and credential Sets will result in an

IllegalStateException

being thrown.
Also, once a

Subject

is read-only,
it can not be reset to being writable again.

**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("setReadOnly")

permission to set this

Subject

to be read-only.

---

#### setReadOnly

public void setReadOnly()

Set this

Subject

to be read-only.

Modifications (additions and removals) to this Subject's

Principal

Set

and
credential Sets will be disallowed.
The

destroy

operation on this Subject's credentials will
still be permitted.

Subsequent attempts to modify the Subject's

Principal

and credential Sets will result in an

IllegalStateException

being thrown.
Also, once a

Subject

is read-only,
it can not be reset to being writable again.

Modifications (additions and removals) to this Subject's

Principal

Set

and
credential Sets will be disallowed.
The

destroy

operation on this Subject's credentials will
still be permitted.

Subsequent attempts to modify the Subject's

Principal

and credential Sets will result in an

IllegalStateException

being thrown.
Also, once a

Subject

is read-only,
it can not be reset to being writable again.

Subsequent attempts to modify the Subject's

Principal

and credential Sets will result in an

IllegalStateException

being thrown.
Also, once a

Subject

is read-only,
it can not be reset to being writable again.

isReadOnly

```java
public boolean isReadOnly()
```

Query whether this

Subject

is read-only.

**Returns:** true if this

Subject

is read-only, false otherwise.

---

#### isReadOnly

public boolean isReadOnly()

Query whether this

Subject

is read-only.

getSubject

```java
public static
Subject
getSubject​(
AccessControlContext
acc)
```

Get the

Subject

associated with the provided

AccessControlContext

.

The

AccessControlContext

may contain many
Subjects (from nested

doAs

calls).
In this situation, the most recent

Subject

associated
with the

AccessControlContext

is returned.

**Parameters:** acc

- the

AccessControlContext

from which to retrieve
the

Subject

.
**Returns:** the

Subject

associated with the provided

AccessControlContext

, or

null

if no

Subject

is associated
with the provided

AccessControlContext

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("getSubject")

permission to get the

Subject

.
**Throws:** NullPointerException

- if the provided

AccessControlContext

is

null

.

---

#### getSubject

public static

Subject

getSubject​(

AccessControlContext

acc)

Get the

Subject

associated with the provided

AccessControlContext

.

The

AccessControlContext

may contain many
Subjects (from nested

doAs

calls).
In this situation, the most recent

Subject

associated
with the

AccessControlContext

is returned.

The

AccessControlContext

may contain many
Subjects (from nested

doAs

calls).
In this situation, the most recent

Subject

associated
with the

AccessControlContext

is returned.

doAs

```java
public static <T> T doAs​(
Subject
subject,

PrivilegedAction
<T> action)
```

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedAction

,
as well as the newly constructed

AccessControlContext

.

**Type Parameters:** T

- the type of the value returned by the PrivilegedAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Returns:** the value returned by the PrivilegedAction's

run

method.
**Throws:** NullPointerException

- if the

PrivilegedAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("doAs")

permission to invoke this
method.

---

#### doAs

public static <T> T doAs​(

Subject

subject,

PrivilegedAction

<T> action)

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedAction

,
as well as the newly constructed

AccessControlContext

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedAction

,
as well as the newly constructed

AccessControlContext

.

doAs

```java
public static <T> T doAs​(
Subject
subject,

PrivilegedExceptionAction
<T> action)
throws
PrivilegedActionException
```

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedExceptionAction

,
as well as the newly constructed

AccessControlContext

.

**Type Parameters:** T

- the type of the value returned by the
PrivilegedExceptionAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Returns:** the value returned by the
PrivilegedExceptionAction's

run

method.
**Throws:** PrivilegedActionException

- if the

PrivilegedExceptionAction.run

method throws a checked exception.
**Throws:** NullPointerException

- if the specified

PrivilegedExceptionAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have an

AuthPermission("doAs")

permission to invoke this
method.

---

#### doAs

public static <T> T doAs​(

Subject

subject,

PrivilegedExceptionAction

<T> action)
throws

PrivilegedActionException

Perform work as a particular

Subject

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedExceptionAction

,
as well as the newly constructed

AccessControlContext

.

This method first retrieves the current Thread's

AccessControlContext

via

AccessController.getContext

,
and then instantiates a new

AccessControlContext

using the retrieved context along with a new

SubjectDomainCombiner

(constructed using
the provided

Subject

).
Finally, this method invokes

AccessController.doPrivileged

,
passing it the provided

PrivilegedExceptionAction

,
as well as the newly constructed

AccessControlContext

.

doAsPrivileged

```java
public static <T> T doAsPrivileged​(
Subject
subject,

PrivilegedAction
<T> action,

AccessControlContext
acc)
```

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

**Type Parameters:** T

- the type of the value returned by the PrivilegedAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Parameters:** acc

- the

AccessControlContext

to be tied to the
specified

subject

and

action

.
**Returns:** the value returned by the PrivilegedAction's

run

method.
**Throws:** NullPointerException

- if the

PrivilegedAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

AuthPermission("doAsPrivileged")

permission to invoke
this method.

---

#### doAsPrivileged

public static <T> T doAsPrivileged​(

Subject

subject,

PrivilegedAction

<T> action,

AccessControlContext

acc)

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

doAsPrivileged

```java
public static <T> T doAsPrivileged​(
Subject
subject,

PrivilegedExceptionAction
<T> action,

AccessControlContext
acc)
throws
PrivilegedActionException
```

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

**Type Parameters:** T

- the type of the value returned by the
PrivilegedExceptionAction's

run

method.
**Parameters:** subject

- the

Subject

that the specified

action

will run as. This parameter
may be

null

.
**Parameters:** action

- the code to be run as the specified

Subject

.
**Parameters:** acc

- the

AccessControlContext

to be tied to the
specified

subject

and

action

.
**Returns:** the value returned by the
PrivilegedExceptionAction's

run

method.
**Throws:** PrivilegedActionException

- if the

PrivilegedExceptionAction.run

method throws a checked exception.
**Throws:** NullPointerException

- if the specified

PrivilegedExceptionAction

is

null

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

AuthPermission("doAsPrivileged")

permission to invoke
this method.

---

#### doAsPrivileged

public static <T> T doAsPrivileged​(

Subject

subject,

PrivilegedExceptionAction

<T> action,

AccessControlContext

acc)
throws

PrivilegedActionException

Perform privileged work as a particular

Subject

.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

This method behaves exactly as

Subject.doAs

,
except that instead of retrieving the current Thread's

AccessControlContext

, it uses the provided

AccessControlContext

. If the provided

AccessControlContext

is

null

,
this method instantiates a new

AccessControlContext

with an empty collection of ProtectionDomains.

getPrincipals

```java
public
Set
<
Principal
> getPrincipals()
```

Return the

Set

of Principals associated with this

Subject

. Each

Principal

represents
an identity for this

Subject

.

The returned

Set

is backed by this Subject's
internal

Principal

Set

. Any modification
to the returned

Set

affects the internal

Principal

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrincipals")

permission to modify
the returned set, or a

SecurityException

will be thrown.

**Returns:** the

Set

of Principals associated with this

Subject

.

---

#### getPrincipals

public

Set

<

Principal

> getPrincipals()

Return the

Set

of Principals associated with this

Subject

. Each

Principal

represents
an identity for this

Subject

.

The returned

Set

is backed by this Subject's
internal

Principal

Set

. Any modification
to the returned

Set

affects the internal

Principal

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrincipals")

permission to modify
the returned set, or a

SecurityException

will be thrown.

The returned

Set

is backed by this Subject's
internal

Principal

Set

. Any modification
to the returned

Set

affects the internal

Principal

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrincipals")

permission to modify
the returned set, or a

SecurityException

will be thrown.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrincipals")

permission to modify
the returned set, or a

SecurityException

will be thrown.

getPrincipals

```java
public <T extends
Principal
>
Set
<T> getPrincipals​(
Class
<T> c)
```

Return a

Set

of Principals associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal

Principal

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal

Principal

Set

.

**Type Parameters:** T

- the type of the class modeled by

c
**Parameters:** c

- the returned

Set

of Principals will all be
instances of this class.
**Returns:** a

Set

of Principals that are instances of the
specified

Class

.
**Throws:** NullPointerException

- if the specified

Class

is

null

.

---

#### getPrincipals

public <T extends

Principal

>

Set

<T> getPrincipals​(

Class

<T> c)

Return a

Set

of Principals associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal

Principal

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal

Principal

Set

.

The returned

Set

is not backed by this Subject's
internal

Principal

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal

Principal

Set

.

getPublicCredentials

```java
public
Set
<
Object
> getPublicCredentials()
```

Return the

Set

of public credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal public Credential

Set

. Any modification
to the returned

Set

affects the internal public
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPublicCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

**Returns:** a

Set

of public credentials held by this

Subject

.

---

#### getPublicCredentials

public

Set

<

Object

> getPublicCredentials()

Return the

Set

of public credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal public Credential

Set

. Any modification
to the returned

Set

affects the internal public
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPublicCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

The returned

Set

is backed by this Subject's
internal public Credential

Set

. Any modification
to the returned

Set

affects the internal public
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPublicCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

If a security manager is installed, the caller must have a

AuthPermission("modifyPublicCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

getPrivateCredentials

```java
public
Set
<
Object
> getPrivateCredentials()
```

Return the

Set

of private credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal private Credential

Set

. Any modification
to the returned

Set

affects the internal private
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrivateCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

While iterating through the

Set

,
a

SecurityException

is thrown if a security manager is installed
and the caller does not have a

PrivateCredentialPermission

to access a particular Credential. The

Iterator

is nevertheless advanced to the next element in the

Set

.

**Returns:** a

Set

of private credentials held by this

Subject

.

---

#### getPrivateCredentials

public

Set

<

Object

> getPrivateCredentials()

Return the

Set

of private credentials held by this

Subject

.

The returned

Set

is backed by this Subject's
internal private Credential

Set

. Any modification
to the returned

Set

affects the internal private
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrivateCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

While iterating through the

Set

,
a

SecurityException

is thrown if a security manager is installed
and the caller does not have a

PrivateCredentialPermission

to access a particular Credential. The

Iterator

is nevertheless advanced to the next element in the

Set

.

The returned

Set

is backed by this Subject's
internal private Credential

Set

. Any modification
to the returned

Set

affects the internal private
Credential

Set

as well.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrivateCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

While iterating through the

Set

,
a

SecurityException

is thrown if a security manager is installed
and the caller does not have a

PrivateCredentialPermission

to access a particular Credential. The

Iterator

is nevertheless advanced to the next element in the

Set

.

If a security manager is installed, the caller must have a

AuthPermission("modifyPrivateCredentials")

permission to modify
the returned set, or a

SecurityException

will be thrown.

While iterating through the

Set

,
a

SecurityException

is thrown if a security manager is installed
and the caller does not have a

PrivateCredentialPermission

to access a particular Credential. The

Iterator

is nevertheless advanced to the next element in the

Set

.

While iterating through the

Set

,
a

SecurityException

is thrown if a security manager is installed
and the caller does not have a

PrivateCredentialPermission

to access a particular Credential. The

Iterator

is nevertheless advanced to the next element in the

Set

.

getPublicCredentials

```java
public <T>
Set
<T> getPublicCredentials​(
Class
<T> c)
```

Return a

Set

of public credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal public Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal public Credential

Set

.

**Type Parameters:** T

- the type of the class modeled by

c
**Parameters:** c

- the returned

Set

of public credentials will all be
instances of this class.
**Returns:** a

Set

of public credentials that are instances
of the specified

Class

.
**Throws:** NullPointerException

- if the specified

Class

is

null

.

---

#### getPublicCredentials

public <T>

Set

<T> getPublicCredentials​(

Class

<T> c)

Return a

Set

of public credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

The returned

Set

is not backed by this Subject's
internal public Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal public Credential

Set

.

The returned

Set

is not backed by this Subject's
internal public Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal public Credential

Set

.

getPrivateCredentials

```java
public <T>
Set
<T> getPrivateCredentials​(
Class
<T> c)
```

Return a

Set

of private credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

If a security manager is installed, the caller must have a

PrivateCredentialPermission

to access all of the requested
Credentials, or a

SecurityException

will be thrown.

The returned

Set

is not backed by this Subject's
internal private Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal private Credential

Set

.

**Type Parameters:** T

- the type of the class modeled by

c
**Parameters:** c

- the returned

Set

of private credentials will all be
instances of this class.
**Returns:** a

Set

of private credentials that are instances
of the specified

Class

.
**Throws:** NullPointerException

- if the specified

Class

is

null

.

---

#### getPrivateCredentials

public <T>

Set

<T> getPrivateCredentials​(

Class

<T> c)

Return a

Set

of private credentials associated with this

Subject

that are instances or subclasses of the specified

Class

.

If a security manager is installed, the caller must have a

PrivateCredentialPermission

to access all of the requested
Credentials, or a

SecurityException

will be thrown.

The returned

Set

is not backed by this Subject's
internal private Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal private Credential

Set

.

If a security manager is installed, the caller must have a

PrivateCredentialPermission

to access all of the requested
Credentials, or a

SecurityException

will be thrown.

The returned

Set

is not backed by this Subject's
internal private Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal private Credential

Set

.

The returned

Set

is not backed by this Subject's
internal private Credential

Set

. A new

Set

is created and returned for each method invocation.
Modifications to the returned

Set

will not affect the internal private Credential

Set

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

Subject

for equality. Returns true if the given object is also a Subject
and the two

Subject

instances are equivalent.
More formally, two

Subject

instances are
equal if their

Principal

and

Credential

Sets are equal.

**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

Subject

.
**Returns:** true if the specified Object is equal to this

Subject

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

PrivateCredentialPermission

permission to access the private credentials for this

Subject

or the provided

Subject

.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares the specified Object with this

Subject

for equality. Returns true if the given object is also a Subject
and the two

Subject

instances are equivalent.
More formally, two

Subject

instances are
equal if their

Principal

and

Credential

Sets are equal.

toString

```java
public
String
toString()
```

Return the String representation of this

Subject

.

**Overrides:** toString

in class

Object
**Returns:** the String representation of this

Subject

.

---

#### toString

public

String

toString()

Return the String representation of this

Subject

.

hashCode

```java
public int hashCode()
```

Returns a hashcode for this

Subject

.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode for this

Subject

.
**Throws:** SecurityException

- if a security manager is installed and the
caller does not have a

PrivateCredentialPermission

permission to access this Subject's private credentials.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode for this

Subject

.

---

