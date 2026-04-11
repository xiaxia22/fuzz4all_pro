# Class PrivateCredentialPermission

**Source:** `java.base\javax\security\auth\PrivateCredentialPermission.html`

### Class Description

```java
public final class
PrivateCredentialPermission

extends
Permission
```

This class is used to protect access to private Credentials
belonging to a particular

Subject

. The

Subject

is represented by a Set of Principals.

The target name of this

Permission

specifies
a Credential class name, and a Set of Principals.
The only valid value for this Permission's actions is, "read".
The target name must abide by the following syntax:

```java
CredentialClass {PrincipalClass "PrincipalName"}*
```

For example, the following permission grants access to the
com.sun.PrivateCredential owned by Subjects which have
a com.sun.Principal with the name, "duke". Note that although
this example, as well as all the examples below, do not contain
Codebase, SignedBy, or Principal information in the grant statement
(for simplicity reasons), actual policy configurations should
specify that information when appropriate.

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"com.sun.PrivateCredential com.sun.Principal \"duke\"",
"read";
};
```

If CredentialClass is "*", then access is granted to
all private Credentials belonging to the specified

Subject

.
If "PrincipalName" is "*", then access is granted to the
specified Credential owned by any

Subject

that has the
specified

Principal

(the actual PrincipalName doesn't matter).
For example, the following grants access to the
a.b.Credential owned by any

Subject

that has
an a.b.Principal.

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "*"",
"read";
};
```

If both the PrincipalClass and "PrincipalName" are "*",
then access is granted to the specified Credential owned by
any

Subject

.

In addition, the PrincipalClass/PrincipalName pairing may be repeated:

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "duke" c.d.Principal "dukette"",
"read";
};
```

The above grants access to the private Credential, "a.b.Credential",
belonging to a

Subject

with at least two associated Principals:
"a.b.Principal" with the name, "duke", and "c.d.Principal", with the name,
"dukette".

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrivateCredentialPermission​(
String
name,

String
actions)

Creates a new

PrivateCredentialPermission

with the specified

name

. The

name

specifies both a Credential class and a

Principal

Set.

**Parameters:**
- name

- the name specifying the Credential class and

Principal

Set.
- actions

- the actions specifying that the Credential can be read.

**Throws:**
- IllegalArgumentException

- if

name

does not conform
to the correct syntax or if

actions

is not "read".

---

### Method Details

#### public
String
getCredentialClass()

Returns the Class name of the Credential associated with this

PrivateCredentialPermission

.

**Returns:**
- the Class name of the Credential associated with this

PrivateCredentialPermission

.

---

#### public
String
[][] getPrincipals()

Returns the

Principal

classes and names
associated with this

PrivateCredentialPermission

.
The information is returned as a two-dimensional array (array[x][y]).
The 'x' value corresponds to the number of

Principal

class and name pairs. When (y==0), it corresponds to
the

Principal

class value, and when (y==1),
it corresponds to the

Principal

name value.
For example, array[0][0] corresponds to the class name of
the first

Principal

in the array. array[0][1]
corresponds to the

Principal

name of the
first

Principal

in the array.

**Returns:**
- the

Principal

class and names associated
with this

PrivateCredentialPermission

.

---

#### public boolean implies​(
Permission
p)

Checks if this

PrivateCredentialPermission

implies
the specified

Permission

.

This method returns true if:

- p

is an instanceof PrivateCredentialPermission and

the target name for

p

is implied by this object's
target name. For example:

```java
[* P1 "duke"] implies [a.b.Credential P1 "duke"].
[C1 P1 "duke"] implies [C1 P1 "duke" P2 "dukette"].
[C1 P2 "dukette"] implies [C1 P1 "duke" P2 "dukette"].
```

**Specified by:**
- implies

in class

Permission

**Parameters:**
- p

- the

Permission

to check against.

**Returns:**
- true if this

PrivateCredentialPermission

implies
the specified

Permission

, false if not.

---

#### public boolean equals​(
Object
obj)

Checks two

PrivateCredentialPermission

objects for
equality. Checks that

obj

is a

PrivateCredentialPermission

,
and has the same credential class as this object,
as well as the same Principals as this object.
The order of the Principals in the respective Permission's
target names is not relevant.

**Specified by:**
- equals

in class

Permission

**Parameters:**
- obj

- the object we are testing for equality with this object.

**Returns:**
- true if obj is a

PrivateCredentialPermission

,
has the same credential class as this object,
and has the same Principals as this object.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this object.

**Specified by:**
- hashCode

in class

Permission

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
getActions()

Returns the "canonical string representation" of the actions.
This method always returns the String, "read".

**Specified by:**
- getActions

in class

Permission

**Returns:**
- the actions (always returns "read").

---

#### public
PermissionCollection
newPermissionCollection()

Return a homogeneous collection of PrivateCredentialPermissions
in a

PermissionCollection

.
No such

PermissionCollection

is defined,
so this method always returns

null

.

**Overrides:**
- newPermissionCollection

in class

Permission

**Returns:**
- null in all cases.

---

### Additional Sections

#### Class PrivateCredentialPermission

java.lang.Object

- java.security.Permission
- - javax.security.auth.PrivateCredentialPermission

java.security.Permission

- javax.security.auth.PrivateCredentialPermission

javax.security.auth.PrivateCredentialPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
PrivateCredentialPermission

extends
Permission
```

This class is used to protect access to private Credentials
belonging to a particular

Subject

. The

Subject

is represented by a Set of Principals.

The target name of this

Permission

specifies
a Credential class name, and a Set of Principals.
The only valid value for this Permission's actions is, "read".
The target name must abide by the following syntax:

```java
CredentialClass {PrincipalClass "PrincipalName"}*
```

For example, the following permission grants access to the
com.sun.PrivateCredential owned by Subjects which have
a com.sun.Principal with the name, "duke". Note that although
this example, as well as all the examples below, do not contain
Codebase, SignedBy, or Principal information in the grant statement
(for simplicity reasons), actual policy configurations should
specify that information when appropriate.

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"com.sun.PrivateCredential com.sun.Principal \"duke\"",
"read";
};
```

If CredentialClass is "*", then access is granted to
all private Credentials belonging to the specified

Subject

.
If "PrincipalName" is "*", then access is granted to the
specified Credential owned by any

Subject

that has the
specified

Principal

(the actual PrincipalName doesn't matter).
For example, the following grants access to the
a.b.Credential owned by any

Subject

that has
an a.b.Principal.

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "*"",
"read";
};
```

If both the PrincipalClass and "PrincipalName" are "*",
then access is granted to the specified Credential owned by
any

Subject

.

In addition, the PrincipalClass/PrincipalName pairing may be repeated:

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "duke" c.d.Principal "dukette"",
"read";
};
```

The above grants access to the private Credential, "a.b.Credential",
belonging to a

Subject

with at least two associated Principals:
"a.b.Principal" with the name, "duke", and "c.d.Principal", with the name,
"dukette".

**Since:** 1.4
**See Also:** Serialized Form

public final class

PrivateCredentialPermission

extends

Permission

This class is used to protect access to private Credentials
belonging to a particular

Subject

. The

Subject

is represented by a Set of Principals.

The target name of this

Permission

specifies
a Credential class name, and a Set of Principals.
The only valid value for this Permission's actions is, "read".
The target name must abide by the following syntax:

```java
CredentialClass {PrincipalClass "PrincipalName"}*
```

For example, the following permission grants access to the
com.sun.PrivateCredential owned by Subjects which have
a com.sun.Principal with the name, "duke". Note that although
this example, as well as all the examples below, do not contain
Codebase, SignedBy, or Principal information in the grant statement
(for simplicity reasons), actual policy configurations should
specify that information when appropriate.

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"com.sun.PrivateCredential com.sun.Principal \"duke\"",
"read";
};
```

If CredentialClass is "*", then access is granted to
all private Credentials belonging to the specified

Subject

.
If "PrincipalName" is "*", then access is granted to the
specified Credential owned by any

Subject

that has the
specified

Principal

(the actual PrincipalName doesn't matter).
For example, the following grants access to the
a.b.Credential owned by any

Subject

that has
an a.b.Principal.

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "*"",
"read";
};
```

If both the PrincipalClass and "PrincipalName" are "*",
then access is granted to the specified Credential owned by
any

Subject

.

In addition, the PrincipalClass/PrincipalName pairing may be repeated:

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "duke" c.d.Principal "dukette"",
"read";
};
```

The above grants access to the private Credential, "a.b.Credential",
belonging to a

Subject

with at least two associated Principals:
"a.b.Principal" with the name, "duke", and "c.d.Principal", with the name,
"dukette".

The target name of this

Permission

specifies
a Credential class name, and a Set of Principals.
The only valid value for this Permission's actions is, "read".
The target name must abide by the following syntax:

```java
CredentialClass {PrincipalClass "PrincipalName"}*
```

For example, the following permission grants access to the
com.sun.PrivateCredential owned by Subjects which have
a com.sun.Principal with the name, "duke". Note that although
this example, as well as all the examples below, do not contain
Codebase, SignedBy, or Principal information in the grant statement
(for simplicity reasons), actual policy configurations should
specify that information when appropriate.

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"com.sun.PrivateCredential com.sun.Principal \"duke\"",
"read";
};
```

If CredentialClass is "*", then access is granted to
all private Credentials belonging to the specified

Subject

.
If "PrincipalName" is "*", then access is granted to the
specified Credential owned by any

Subject

that has the
specified

Principal

(the actual PrincipalName doesn't matter).
For example, the following grants access to the
a.b.Credential owned by any

Subject

that has
an a.b.Principal.

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "*"",
"read";
};
```

If both the PrincipalClass and "PrincipalName" are "*",
then access is granted to the specified Credential owned by
any

Subject

.

In addition, the PrincipalClass/PrincipalName pairing may be repeated:

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "duke" c.d.Principal "dukette"",
"read";
};
```

The above grants access to the private Credential, "a.b.Credential",
belonging to a

Subject

with at least two associated Principals:
"a.b.Principal" with the name, "duke", and "c.d.Principal", with the name,
"dukette".

CredentialClass {PrincipalClass "PrincipalName"}*

grant {
permission javax.security.auth.PrivateCredentialPermission
"com.sun.PrivateCredential com.sun.Principal \"duke\"",
"read";
};

grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "*"",
"read";
};

In addition, the PrincipalClass/PrincipalName pairing may be repeated:

```java
grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "duke" c.d.Principal "dukette"",
"read";
};
```

The above grants access to the private Credential, "a.b.Credential",
belonging to a

Subject

with at least two associated Principals:
"a.b.Principal" with the name, "duke", and "c.d.Principal", with the name,
"dukette".

grant {
permission javax.security.auth.PrivateCredentialPermission
"a.b.Credential a.b.Principal "duke" c.d.Principal "dukette"",
"read";
};

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrivateCredentialPermission

​(

String

name,

String

actions)

Creates a new

PrivateCredentialPermission

with the specified

name

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two

PrivateCredentialPermission

objects for
equality.

String

getActions

()

Returns the "canonical string representation" of the actions.

String

getCredentialClass

()

Returns the Class name of the Credential associated with this

PrivateCredentialPermission

.

String

[][]

getPrincipals

()

Returns the

Principal

classes and names
associated with this

PrivateCredentialPermission

.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this

PrivateCredentialPermission

implies
the specified

Permission

.

PermissionCollection

newPermissionCollection

()

Return a homogeneous collection of PrivateCredentialPermissions
in a

PermissionCollection

.

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

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

PrivateCredentialPermission

​(

String

name,

String

actions)

Creates a new

PrivateCredentialPermission

with the specified

name

.

---

#### Constructor Summary

Creates a new

PrivateCredentialPermission

with the specified

name

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two

PrivateCredentialPermission

objects for
equality.

String

getActions

()

Returns the "canonical string representation" of the actions.

String

getCredentialClass

()

Returns the Class name of the Credential associated with this

PrivateCredentialPermission

.

String

[][]

getPrincipals

()

Returns the

Principal

classes and names
associated with this

PrivateCredentialPermission

.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this

PrivateCredentialPermission

implies
the specified

Permission

.

PermissionCollection

newPermissionCollection

()

Return a homogeneous collection of PrivateCredentialPermissions
in a

PermissionCollection

.

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

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

Checks two

PrivateCredentialPermission

objects for
equality.

Returns the "canonical string representation" of the actions.

Returns the Class name of the Credential associated with this

PrivateCredentialPermission

.

Returns the

Principal

classes and names
associated with this

PrivateCredentialPermission

.

Returns the hash code value for this object.

Checks if this

PrivateCredentialPermission

implies
the specified

Permission

.

Return a homogeneous collection of PrivateCredentialPermissions
in a

PermissionCollection

.

Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

---

#### Methods declared in class java.security. Permission

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

- PrivateCredentialPermission

```java
public PrivateCredentialPermission​(
String
name,

String
actions)
```

Creates a new

PrivateCredentialPermission

with the specified

name

. The

name

specifies both a Credential class and a

Principal

Set.

**Parameters:** name

- the name specifying the Credential class and

Principal

Set.
**Parameters:** actions

- the actions specifying that the Credential can be read.
**Throws:** IllegalArgumentException

- if

name

does not conform
to the correct syntax or if

actions

is not "read".

============ METHOD DETAIL ==========

- Method Detail

- getCredentialClass

```java
public
String
getCredentialClass()
```

Returns the Class name of the Credential associated with this

PrivateCredentialPermission

.

**Returns:** the Class name of the Credential associated with this

PrivateCredentialPermission

.

- getPrincipals

```java
public
String
[][] getPrincipals()
```

Returns the

Principal

classes and names
associated with this

PrivateCredentialPermission

.
The information is returned as a two-dimensional array (array[x][y]).
The 'x' value corresponds to the number of

Principal

class and name pairs. When (y==0), it corresponds to
the

Principal

class value, and when (y==1),
it corresponds to the

Principal

name value.
For example, array[0][0] corresponds to the class name of
the first

Principal

in the array. array[0][1]
corresponds to the

Principal

name of the
first

Principal

in the array.

**Returns:** the

Principal

class and names associated
with this

PrivateCredentialPermission

.

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this

PrivateCredentialPermission

implies
the specified

Permission

.

This method returns true if:

- p

is an instanceof PrivateCredentialPermission and

the target name for

p

is implied by this object's
target name. For example:

```java
[* P1 "duke"] implies [a.b.Credential P1 "duke"].
[C1 P1 "duke"] implies [C1 P1 "duke" P2 "dukette"].
[C1 P2 "dukette"] implies [C1 P1 "duke" P2 "dukette"].
```

**Specified by:** implies

in class

Permission
**Parameters:** p

- the

Permission

to check against.
**Returns:** true if this

PrivateCredentialPermission

implies
the specified

Permission

, false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two

PrivateCredentialPermission

objects for
equality. Checks that

obj

is a

PrivateCredentialPermission

,
and has the same credential class as this object,
as well as the same Principals as this object.
The order of the Principals in the respective Permission's
target names is not relevant.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if obj is a

PrivateCredentialPermission

,
has the same credential class as this object,
and has the same Principals as this object.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the "canonical string representation" of the actions.
This method always returns the String, "read".

**Specified by:** getActions

in class

Permission
**Returns:** the actions (always returns "read").

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Return a homogeneous collection of PrivateCredentialPermissions
in a

PermissionCollection

.
No such

PermissionCollection

is defined,
so this method always returns

null

.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** null in all cases.

Constructor Detail

- PrivateCredentialPermission

```java
public PrivateCredentialPermission​(
String
name,

String
actions)
```

Creates a new

PrivateCredentialPermission

with the specified

name

. The

name

specifies both a Credential class and a

Principal

Set.

**Parameters:** name

- the name specifying the Credential class and

Principal

Set.
**Parameters:** actions

- the actions specifying that the Credential can be read.
**Throws:** IllegalArgumentException

- if

name

does not conform
to the correct syntax or if

actions

is not "read".

---

#### Constructor Detail

PrivateCredentialPermission

```java
public PrivateCredentialPermission​(
String
name,

String
actions)
```

Creates a new

PrivateCredentialPermission

with the specified

name

. The

name

specifies both a Credential class and a

Principal

Set.

**Parameters:** name

- the name specifying the Credential class and

Principal

Set.
**Parameters:** actions

- the actions specifying that the Credential can be read.
**Throws:** IllegalArgumentException

- if

name

does not conform
to the correct syntax or if

actions

is not "read".

---

#### PrivateCredentialPermission

public PrivateCredentialPermission​(

String

name,

String

actions)

Creates a new

PrivateCredentialPermission

with the specified

name

. The

name

specifies both a Credential class and a

Principal

Set.

Method Detail

- getCredentialClass

```java
public
String
getCredentialClass()
```

Returns the Class name of the Credential associated with this

PrivateCredentialPermission

.

**Returns:** the Class name of the Credential associated with this

PrivateCredentialPermission

.

- getPrincipals

```java
public
String
[][] getPrincipals()
```

Returns the

Principal

classes and names
associated with this

PrivateCredentialPermission

.
The information is returned as a two-dimensional array (array[x][y]).
The 'x' value corresponds to the number of

Principal

class and name pairs. When (y==0), it corresponds to
the

Principal

class value, and when (y==1),
it corresponds to the

Principal

name value.
For example, array[0][0] corresponds to the class name of
the first

Principal

in the array. array[0][1]
corresponds to the

Principal

name of the
first

Principal

in the array.

**Returns:** the

Principal

class and names associated
with this

PrivateCredentialPermission

.

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this

PrivateCredentialPermission

implies
the specified

Permission

.

This method returns true if:

- p

is an instanceof PrivateCredentialPermission and

the target name for

p

is implied by this object's
target name. For example:

```java
[* P1 "duke"] implies [a.b.Credential P1 "duke"].
[C1 P1 "duke"] implies [C1 P1 "duke" P2 "dukette"].
[C1 P2 "dukette"] implies [C1 P1 "duke" P2 "dukette"].
```

**Specified by:** implies

in class

Permission
**Parameters:** p

- the

Permission

to check against.
**Returns:** true if this

PrivateCredentialPermission

implies
the specified

Permission

, false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two

PrivateCredentialPermission

objects for
equality. Checks that

obj

is a

PrivateCredentialPermission

,
and has the same credential class as this object,
as well as the same Principals as this object.
The order of the Principals in the respective Permission's
target names is not relevant.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if obj is a

PrivateCredentialPermission

,
has the same credential class as this object,
and has the same Principals as this object.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the "canonical string representation" of the actions.
This method always returns the String, "read".

**Specified by:** getActions

in class

Permission
**Returns:** the actions (always returns "read").

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Return a homogeneous collection of PrivateCredentialPermissions
in a

PermissionCollection

.
No such

PermissionCollection

is defined,
so this method always returns

null

.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** null in all cases.

---

#### Method Detail

getCredentialClass

```java
public
String
getCredentialClass()
```

Returns the Class name of the Credential associated with this

PrivateCredentialPermission

.

**Returns:** the Class name of the Credential associated with this

PrivateCredentialPermission

.

---

#### getCredentialClass

public

String

getCredentialClass()

Returns the Class name of the Credential associated with this

PrivateCredentialPermission

.

getPrincipals

```java
public
String
[][] getPrincipals()
```

Returns the

Principal

classes and names
associated with this

PrivateCredentialPermission

.
The information is returned as a two-dimensional array (array[x][y]).
The 'x' value corresponds to the number of

Principal

class and name pairs. When (y==0), it corresponds to
the

Principal

class value, and when (y==1),
it corresponds to the

Principal

name value.
For example, array[0][0] corresponds to the class name of
the first

Principal

in the array. array[0][1]
corresponds to the

Principal

name of the
first

Principal

in the array.

**Returns:** the

Principal

class and names associated
with this

PrivateCredentialPermission

.

---

#### getPrincipals

public

String

[][] getPrincipals()

Returns the

Principal

classes and names
associated with this

PrivateCredentialPermission

.
The information is returned as a two-dimensional array (array[x][y]).
The 'x' value corresponds to the number of

Principal

class and name pairs. When (y==0), it corresponds to
the

Principal

class value, and when (y==1),
it corresponds to the

Principal

name value.
For example, array[0][0] corresponds to the class name of
the first

Principal

in the array. array[0][1]
corresponds to the

Principal

name of the
first

Principal

in the array.

implies

```java
public boolean implies​(
Permission
p)
```

Checks if this

PrivateCredentialPermission

implies
the specified

Permission

.

This method returns true if:

- p

is an instanceof PrivateCredentialPermission and

the target name for

p

is implied by this object's
target name. For example:

```java
[* P1 "duke"] implies [a.b.Credential P1 "duke"].
[C1 P1 "duke"] implies [C1 P1 "duke" P2 "dukette"].
[C1 P2 "dukette"] implies [C1 P1 "duke" P2 "dukette"].
```

**Specified by:** implies

in class

Permission
**Parameters:** p

- the

Permission

to check against.
**Returns:** true if this

PrivateCredentialPermission

implies
the specified

Permission

, false if not.

---

#### implies

public boolean implies​(

Permission

p)

Checks if this

PrivateCredentialPermission

implies
the specified

Permission

.

This method returns true if:

- p

is an instanceof PrivateCredentialPermission and

the target name for

p

is implied by this object's
target name. For example:

```java
[* P1 "duke"] implies [a.b.Credential P1 "duke"].
[C1 P1 "duke"] implies [C1 P1 "duke" P2 "dukette"].
[C1 P2 "dukette"] implies [C1 P1 "duke" P2 "dukette"].
```

This method returns true if:

- p

is an instanceof PrivateCredentialPermission and

the target name for

p

is implied by this object's
target name. For example:

```java
[* P1 "duke"] implies [a.b.Credential P1 "duke"].
[C1 P1 "duke"] implies [C1 P1 "duke" P2 "dukette"].
[C1 P2 "dukette"] implies [C1 P1 "duke" P2 "dukette"].
```

p

is an instanceof PrivateCredentialPermission and

the target name for

p

is implied by this object's
target name. For example:

```java
[* P1 "duke"] implies [a.b.Credential P1 "duke"].
[C1 P1 "duke"] implies [C1 P1 "duke" P2 "dukette"].
[C1 P2 "dukette"] implies [C1 P1 "duke" P2 "dukette"].
```

[* P1 "duke"] implies [a.b.Credential P1 "duke"].
[C1 P1 "duke"] implies [C1 P1 "duke" P2 "dukette"].
[C1 P2 "dukette"] implies [C1 P1 "duke" P2 "dukette"].

equals

```java
public boolean equals​(
Object
obj)
```

Checks two

PrivateCredentialPermission

objects for
equality. Checks that

obj

is a

PrivateCredentialPermission

,
and has the same credential class as this object,
as well as the same Principals as this object.
The order of the Principals in the respective Permission's
target names is not relevant.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if obj is a

PrivateCredentialPermission

,
has the same credential class as this object,
and has the same Principals as this object.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks two

PrivateCredentialPermission

objects for
equality. Checks that

obj

is a

PrivateCredentialPermission

,
and has the same credential class as this object,
as well as the same Principals as this object.
The order of the Principals in the respective Permission's
target names is not relevant.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this object.

getActions

```java
public
String
getActions()
```

Returns the "canonical string representation" of the actions.
This method always returns the String, "read".

**Specified by:** getActions

in class

Permission
**Returns:** the actions (always returns "read").

---

#### getActions

public

String

getActions()

Returns the "canonical string representation" of the actions.
This method always returns the String, "read".

newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Return a homogeneous collection of PrivateCredentialPermissions
in a

PermissionCollection

.
No such

PermissionCollection

is defined,
so this method always returns

null

.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** null in all cases.

---

#### newPermissionCollection

public

PermissionCollection

newPermissionCollection()

Return a homogeneous collection of PrivateCredentialPermissions
in a

PermissionCollection

.
No such

PermissionCollection

is defined,
so this method always returns

null

.

---

