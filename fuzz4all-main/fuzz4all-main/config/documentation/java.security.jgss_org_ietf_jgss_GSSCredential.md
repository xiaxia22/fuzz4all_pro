# Interface GSSCredential

**Source:** `java.security.jgss\org\ietf\jgss\GSSCredential.html`

### Class Description

```java
public interface
GSSCredential

extends
Cloneable
```

This interface encapsulates the GSS-API credentials for an entity. A
credential contains all the necessary cryptographic information to
enable the creation of a context on behalf of the entity that it
represents. It may contain multiple, distinct, mechanism specific
credential elements, each containing information for a specific
security mechanism, but all referring to the same entity. A credential
may be used to perform context initiation, acceptance, or both.

Credentials are instantiated using one of the

createCredential

methods in the

GSSManager

class. GSS-API credential creation is not
intended to provide a "login to the network" function, as such a
function would involve the creation of new credentials rather than
merely acquiring a handle to existing credentials. The

section on credential
acquisition

in the package level description describes
how existing credentials are acquired in the Java platform. GSS-API
implementations must impose a local access-control policy on callers to
prevent unauthorized callers from acquiring credentials to which they
are not entitled.

Applications will create a credential object passing the desired
parameters. The application can then use the query methods to obtain
specific information about the instantiated credential object.
When the credential is no longer needed, the application should call
the

dispose

method to release any resources held by
the credential object and to destroy any cryptographically sensitive
information.

This example code demonstrates the creation of a GSSCredential
implementation for a specific entity, querying of its fields, and its
release when it is no longer needed:

```java
GSSManager manager = GSSManager.getInstance();

// start by creating a name object for the entity
GSSName name = manager.createName("myusername", GSSName.NT_USER_NAME);

// now acquire credentials for the entity
GSSCredential cred = manager.createCredential(name,
GSSCredential.ACCEPT_ONLY);

// display credential information - name, remaining lifetime,
// and the mechanisms it has been acquired over
System.out.println(cred.getName().toString());
System.out.println(cred.getRemainingLifetime());

Oid [] mechs = cred.getMechs();
if (mechs != null) {
for (int i = 0; i< mechs.length; i++)
System.out.println(mechs[i].toString());
}

// release system resources held by the credential
cred.dispose();
```

**All Superinterfaces:** Cloneable

---

### Field Details

#### static final int INITIATE_AND_ACCEPT

Credential usage flag requesting that it be usable
for both context initiation and acceptance.

**See Also:**
- Constant Field Values

---

#### static final int INITIATE_ONLY

Credential usage flag requesting that it be usable
for context initiation only.

**See Also:**
- Constant Field Values

---

#### static final int ACCEPT_ONLY

Credential usage flag requesting that it be usable
for context acceptance only.

**See Also:**
- Constant Field Values

---

#### static final int DEFAULT_LIFETIME

A lifetime constant representing the default credential lifetime. This
value it set to 0.

**See Also:**
- Constant Field Values

---

#### static final int INDEFINITE_LIFETIME

A lifetime constant representing indefinite credential lifetime.
This value must is set to the maximum integer value in Java -

Integer.MAX_VALUE

.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void dispose()
throws
GSSException

Releases any sensitive information that the GSSCredential object may
be containing. Applications should call this method as soon as the
credential is no longer needed to minimize the time any sensitive
information is maintained.

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### GSSName
getName()
throws
GSSException

Retrieves the name of the entity that the credential asserts.

**Returns:**
- a GSSName representing the entity

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### GSSName
getName​(
Oid
mech)
throws
GSSException

Retrieves a Mechanism Name of the entity that the credential
asserts. This is equivalent to calling

canonicalize

on the value returned by
the other form of

getName

.

**Parameters:**
- mech

- the Oid of the mechanism for which the Mechanism Name
should be returned.

**Returns:**
- a GSSName representing the entity canonicalized for the
desired mechanism

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

---

#### int getRemainingLifetime()
throws
GSSException

Returns the remaining lifetime in seconds for a credential. The
remaining lifetime is the minimum lifetime amongst all of the underlying
mechanism specific credential elements.

**Returns:**
- the minimum remaining lifetime in seconds for this
credential. A return value of

INDEFINITE_LIFETIME

indicates that the credential does
not expire. A return value of 0 indicates that the credential is
already expired.

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.FAILURE

**See Also:**
- getRemainingInitLifetime(Oid)

,

getRemainingAcceptLifetime(Oid)

---

#### int getRemainingInitLifetime​(
Oid
mech)
throws
GSSException

Returns the lifetime in seconds for the credential to remain capable
of initiating security contexts using the specified mechanism. This
method queries the initiator credential element that belongs to the
specified mechanism.

**Parameters:**
- mech

- the Oid of the mechanism whose initiator credential element
should be queried.

**Returns:**
- the number of seconds remaining in the life of this credential
element. A return value of

INDEFINITE_LIFETIME

indicates that the credential element does not
expire. A return value of 0 indicates that the credential element is
already expired.

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

---

#### int getRemainingAcceptLifetime​(
Oid
mech)
throws
GSSException

Returns the lifetime in seconds for the credential to remain capable
of accepting security contexts using the specified mechanism. This
method queries the acceptor credential element that belongs to the
specified mechanism.

**Parameters:**
- mech

- the Oid of the mechanism whose acceptor credential element
should be queried.

**Returns:**
- the number of seconds remaining in the life of this credential
element. A return value of

INDEFINITE_LIFETIME

indicates that the credential element does not
expire. A return value of 0 indicates that the credential element is
already expired.

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

---

#### int getUsage()
throws
GSSException

Returns the credential usage mode. In other words, it
tells us if this credential can be used for initiating or accepting
security contexts. It does not tell us which mechanism(s) has to be
used in order to do so. It is expected that an application will allow
the GSS-API to pick a default mechanism after calling this method.

**Returns:**
- The return value will be one of

INITIATE_ONLY

,

ACCEPT_ONLY

, and

INITIATE_AND_ACCEPT

.

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### int getUsage​(
Oid
mech)
throws
GSSException

Returns the credential usage mode for a specific mechanism. In other
words, it tells us if this credential can be used
for initiating or accepting security contexts with a given underlying
mechanism.

**Parameters:**
- mech

- the Oid of the mechanism whose credentials usage mode is
to be determined.

**Returns:**
- The return value will be one of

INITIATE_ONLY

,

ACCEPT_ONLY

, and

INITIATE_AND_ACCEPT

.

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

---

#### Oid
[] getMechs()
throws
GSSException

Returns a list of mechanisms supported by this credential. It does
not tell us which ones can be used to initiate
contexts and which ones can be used to accept contexts. The
application must call the

getUsage

method with
each of the returned Oid's to determine the possible modes of
usage.

**Returns:**
- an array of Oid's corresponding to the supported mechanisms.

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### void add​(
GSSName
name,
int initLifetime,
int acceptLifetime,

Oid
mech,
int usage)
throws
GSSException

Adds a mechanism specific credential-element to an existing
credential. This method allows the construction of credentials, one
mechanism at a time.

This routine is envisioned to be used mainly by context acceptors
during the creation of acceptor credentials which are to be used
with a variety of clients using different security mechanisms.

This routine adds the new credential element "in-place". To add the
element in a new credential, first call

clone

to obtain a
copy of this credential, then call its

add

method.

As always, GSS-API implementations must impose a local access-control
policy on callers to prevent unauthorized callers from acquiring
credentials to which they are not entitled.

Non-default values for initLifetime and acceptLifetime cannot always
be honored by the underlying mechanisms, thus callers should be
prepared to call

getRemainingInitLifetime

and

getRemainingAcceptLifetime

on the credential.

**Parameters:**
- name

- the name of the principal for whom this credential is to
be acquired. Use

null

to specify the default
principal.
- initLifetime

- the number of seconds that the credential element
should remain valid for initiating of security contexts. Use

GSSCredential.INDEFINITE_LIFETIME

to request that the credentials have the maximum permitted lifetime
for this. Use

GSSCredential.DEFAULT_LIFETIME

to request default credential lifetime
for this.
- acceptLifetime

- the number of seconds that the credential
element should remain valid for accepting security contexts. Use

GSSCredential.INDEFINITE_LIFETIME

to request that the credentials have the maximum permitted lifetime
for this. Use

GSSCredential.DEFAULT_LIFETIME

to request default credential lifetime
for this.
- mech

- the mechanism over which the credential is to be acquired.
- usage

- the usage mode that this credential
element should add to the credential. The value
of this parameter must be one of:

INITIATE_AND_ACCEPT

,

ACCEPT_ONLY

, and

INITIATE_ONLY

.

**Throws:**
- GSSException

- containing the following
major error codes:

GSSException.DUPLICATE_ELEMENT

,

GSSException.BAD_MECH

,

GSSException.BAD_NAMETYPE

,

GSSException.NO_CRED

,

GSSException.CREDENTIALS_EXPIRED

,

GSSException.FAILURE

---

#### boolean equals​(
Object
another)

Tests if this GSSCredential asserts the same entity as the supplied
object. The two credentials must be acquired over the same
mechanisms and must refer to the same principal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- another

- another GSSCredential for comparison to this one

**Returns:**
- true

if the two GSSCredentials assert the same
entity;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns a hashcode value for this GSSCredential.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashCode value

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Interface GSSCredential

**All Superinterfaces:** Cloneable

**All Known Subinterfaces:** ExtendedGSSCredential

```java
public interface
GSSCredential

extends
Cloneable
```

This interface encapsulates the GSS-API credentials for an entity. A
credential contains all the necessary cryptographic information to
enable the creation of a context on behalf of the entity that it
represents. It may contain multiple, distinct, mechanism specific
credential elements, each containing information for a specific
security mechanism, but all referring to the same entity. A credential
may be used to perform context initiation, acceptance, or both.

Credentials are instantiated using one of the

createCredential

methods in the

GSSManager

class. GSS-API credential creation is not
intended to provide a "login to the network" function, as such a
function would involve the creation of new credentials rather than
merely acquiring a handle to existing credentials. The

section on credential
acquisition

in the package level description describes
how existing credentials are acquired in the Java platform. GSS-API
implementations must impose a local access-control policy on callers to
prevent unauthorized callers from acquiring credentials to which they
are not entitled.

Applications will create a credential object passing the desired
parameters. The application can then use the query methods to obtain
specific information about the instantiated credential object.
When the credential is no longer needed, the application should call
the

dispose

method to release any resources held by
the credential object and to destroy any cryptographically sensitive
information.

This example code demonstrates the creation of a GSSCredential
implementation for a specific entity, querying of its fields, and its
release when it is no longer needed:

```java
GSSManager manager = GSSManager.getInstance();

// start by creating a name object for the entity
GSSName name = manager.createName("myusername", GSSName.NT_USER_NAME);

// now acquire credentials for the entity
GSSCredential cred = manager.createCredential(name,
GSSCredential.ACCEPT_ONLY);

// display credential information - name, remaining lifetime,
// and the mechanisms it has been acquired over
System.out.println(cred.getName().toString());
System.out.println(cred.getRemainingLifetime());

Oid [] mechs = cred.getMechs();
if (mechs != null) {
for (int i = 0; i< mechs.length; i++)
System.out.println(mechs[i].toString());
}

// release system resources held by the credential
cred.dispose();
```

**Since:** 1.4
**See Also:** GSSManager.createCredential(int)

,

GSSManager.createCredential(GSSName, int, Oid, int)

,

GSSManager.createCredential(GSSName, int, Oid[], int)

,

dispose()

public interface

GSSCredential

extends

Cloneable

This interface encapsulates the GSS-API credentials for an entity. A
credential contains all the necessary cryptographic information to
enable the creation of a context on behalf of the entity that it
represents. It may contain multiple, distinct, mechanism specific
credential elements, each containing information for a specific
security mechanism, but all referring to the same entity. A credential
may be used to perform context initiation, acceptance, or both.

Credentials are instantiated using one of the

createCredential

methods in the

GSSManager

class. GSS-API credential creation is not
intended to provide a "login to the network" function, as such a
function would involve the creation of new credentials rather than
merely acquiring a handle to existing credentials. The

section on credential
acquisition

in the package level description describes
how existing credentials are acquired in the Java platform. GSS-API
implementations must impose a local access-control policy on callers to
prevent unauthorized callers from acquiring credentials to which they
are not entitled.

Applications will create a credential object passing the desired
parameters. The application can then use the query methods to obtain
specific information about the instantiated credential object.
When the credential is no longer needed, the application should call
the

dispose

method to release any resources held by
the credential object and to destroy any cryptographically sensitive
information.

This example code demonstrates the creation of a GSSCredential
implementation for a specific entity, querying of its fields, and its
release when it is no longer needed:

```java
GSSManager manager = GSSManager.getInstance();

// start by creating a name object for the entity
GSSName name = manager.createName("myusername", GSSName.NT_USER_NAME);

// now acquire credentials for the entity
GSSCredential cred = manager.createCredential(name,
GSSCredential.ACCEPT_ONLY);

// display credential information - name, remaining lifetime,
// and the mechanisms it has been acquired over
System.out.println(cred.getName().toString());
System.out.println(cred.getRemainingLifetime());

Oid [] mechs = cred.getMechs();
if (mechs != null) {
for (int i = 0; i< mechs.length; i++)
System.out.println(mechs[i].toString());
}

// release system resources held by the credential
cred.dispose();
```

Credentials are instantiated using one of the

createCredential

methods in the

GSSManager

class. GSS-API credential creation is not
intended to provide a "login to the network" function, as such a
function would involve the creation of new credentials rather than
merely acquiring a handle to existing credentials. The

section on credential
acquisition

in the package level description describes
how existing credentials are acquired in the Java platform. GSS-API
implementations must impose a local access-control policy on callers to
prevent unauthorized callers from acquiring credentials to which they
are not entitled.

Applications will create a credential object passing the desired
parameters. The application can then use the query methods to obtain
specific information about the instantiated credential object.
When the credential is no longer needed, the application should call
the

dispose

method to release any resources held by
the credential object and to destroy any cryptographically sensitive
information.

This example code demonstrates the creation of a GSSCredential
implementation for a specific entity, querying of its fields, and its
release when it is no longer needed:

```java
GSSManager manager = GSSManager.getInstance();

// start by creating a name object for the entity
GSSName name = manager.createName("myusername", GSSName.NT_USER_NAME);

// now acquire credentials for the entity
GSSCredential cred = manager.createCredential(name,
GSSCredential.ACCEPT_ONLY);

// display credential information - name, remaining lifetime,
// and the mechanisms it has been acquired over
System.out.println(cred.getName().toString());
System.out.println(cred.getRemainingLifetime());

Oid [] mechs = cred.getMechs();
if (mechs != null) {
for (int i = 0; i< mechs.length; i++)
System.out.println(mechs[i].toString());
}

// release system resources held by the credential
cred.dispose();
```

Applications will create a credential object passing the desired
parameters. The application can then use the query methods to obtain
specific information about the instantiated credential object.
When the credential is no longer needed, the application should call
the

dispose

method to release any resources held by
the credential object and to destroy any cryptographically sensitive
information.

This example code demonstrates the creation of a GSSCredential
implementation for a specific entity, querying of its fields, and its
release when it is no longer needed:

```java
GSSManager manager = GSSManager.getInstance();

// start by creating a name object for the entity
GSSName name = manager.createName("myusername", GSSName.NT_USER_NAME);

// now acquire credentials for the entity
GSSCredential cred = manager.createCredential(name,
GSSCredential.ACCEPT_ONLY);

// display credential information - name, remaining lifetime,
// and the mechanisms it has been acquired over
System.out.println(cred.getName().toString());
System.out.println(cred.getRemainingLifetime());

Oid [] mechs = cred.getMechs();
if (mechs != null) {
for (int i = 0; i< mechs.length; i++)
System.out.println(mechs[i].toString());
}

// release system resources held by the credential
cred.dispose();
```

This example code demonstrates the creation of a GSSCredential
implementation for a specific entity, querying of its fields, and its
release when it is no longer needed:

```java
GSSManager manager = GSSManager.getInstance();

// start by creating a name object for the entity
GSSName name = manager.createName("myusername", GSSName.NT_USER_NAME);

// now acquire credentials for the entity
GSSCredential cred = manager.createCredential(name,
GSSCredential.ACCEPT_ONLY);

// display credential information - name, remaining lifetime,
// and the mechanisms it has been acquired over
System.out.println(cred.getName().toString());
System.out.println(cred.getRemainingLifetime());

Oid [] mechs = cred.getMechs();
if (mechs != null) {
for (int i = 0; i< mechs.length; i++)
System.out.println(mechs[i].toString());
}

// release system resources held by the credential
cred.dispose();
```

GSSManager manager = GSSManager.getInstance();

// start by creating a name object for the entity
GSSName name = manager.createName("myusername", GSSName.NT_USER_NAME);

// now acquire credentials for the entity
GSSCredential cred = manager.createCredential(name,
GSSCredential.ACCEPT_ONLY);

// display credential information - name, remaining lifetime,
// and the mechanisms it has been acquired over
System.out.println(cred.getName().toString());
System.out.println(cred.getRemainingLifetime());

Oid [] mechs = cred.getMechs();
if (mechs != null) {
for (int i = 0; i< mechs.length; i++)
System.out.println(mechs[i].toString());
}

// release system resources held by the credential
cred.dispose();

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ACCEPT_ONLY

Credential usage flag requesting that it be usable
for context acceptance only.

static int

DEFAULT_LIFETIME

A lifetime constant representing the default credential lifetime.

static int

INDEFINITE_LIFETIME

A lifetime constant representing indefinite credential lifetime.

static int

INITIATE_AND_ACCEPT

Credential usage flag requesting that it be usable
for both context initiation and acceptance.

static int

INITIATE_ONLY

Credential usage flag requesting that it be usable
for context initiation only.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(

GSSName

name,
int initLifetime,
int acceptLifetime,

Oid

mech,
int usage)

Adds a mechanism specific credential-element to an existing
credential.

void

dispose

()

Releases any sensitive information that the GSSCredential object may
be containing.

boolean

equals

​(

Object

another)

Tests if this GSSCredential asserts the same entity as the supplied
object.

Oid

[]

getMechs

()

Returns a list of mechanisms supported by this credential.

GSSName

getName

()

Retrieves the name of the entity that the credential asserts.

GSSName

getName

​(

Oid

mech)

Retrieves a Mechanism Name of the entity that the credential
asserts.

int

getRemainingAcceptLifetime

​(

Oid

mech)

Returns the lifetime in seconds for the credential to remain capable
of accepting security contexts using the specified mechanism.

int

getRemainingInitLifetime

​(

Oid

mech)

Returns the lifetime in seconds for the credential to remain capable
of initiating security contexts using the specified mechanism.

int

getRemainingLifetime

()

Returns the remaining lifetime in seconds for a credential.

int

getUsage

()

Returns the credential usage mode.

int

getUsage

​(

Oid

mech)

Returns the credential usage mode for a specific mechanism.

int

hashCode

()

Returns a hashcode value for this GSSCredential.

Field Summary

Fields

Modifier and Type

Field

Description

static int

ACCEPT_ONLY

Credential usage flag requesting that it be usable
for context acceptance only.

static int

DEFAULT_LIFETIME

A lifetime constant representing the default credential lifetime.

static int

INDEFINITE_LIFETIME

A lifetime constant representing indefinite credential lifetime.

static int

INITIATE_AND_ACCEPT

Credential usage flag requesting that it be usable
for both context initiation and acceptance.

static int

INITIATE_ONLY

Credential usage flag requesting that it be usable
for context initiation only.

---

#### Field Summary

Credential usage flag requesting that it be usable
for context acceptance only.

A lifetime constant representing the default credential lifetime.

A lifetime constant representing indefinite credential lifetime.

Credential usage flag requesting that it be usable
for both context initiation and acceptance.

Credential usage flag requesting that it be usable
for context initiation only.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(

GSSName

name,
int initLifetime,
int acceptLifetime,

Oid

mech,
int usage)

Adds a mechanism specific credential-element to an existing
credential.

void

dispose

()

Releases any sensitive information that the GSSCredential object may
be containing.

boolean

equals

​(

Object

another)

Tests if this GSSCredential asserts the same entity as the supplied
object.

Oid

[]

getMechs

()

Returns a list of mechanisms supported by this credential.

GSSName

getName

()

Retrieves the name of the entity that the credential asserts.

GSSName

getName

​(

Oid

mech)

Retrieves a Mechanism Name of the entity that the credential
asserts.

int

getRemainingAcceptLifetime

​(

Oid

mech)

Returns the lifetime in seconds for the credential to remain capable
of accepting security contexts using the specified mechanism.

int

getRemainingInitLifetime

​(

Oid

mech)

Returns the lifetime in seconds for the credential to remain capable
of initiating security contexts using the specified mechanism.

int

getRemainingLifetime

()

Returns the remaining lifetime in seconds for a credential.

int

getUsage

()

Returns the credential usage mode.

int

getUsage

​(

Oid

mech)

Returns the credential usage mode for a specific mechanism.

int

hashCode

()

Returns a hashcode value for this GSSCredential.

---

#### Method Summary

Adds a mechanism specific credential-element to an existing
credential.

Releases any sensitive information that the GSSCredential object may
be containing.

Tests if this GSSCredential asserts the same entity as the supplied
object.

Returns a list of mechanisms supported by this credential.

Retrieves the name of the entity that the credential asserts.

Retrieves a Mechanism Name of the entity that the credential
asserts.

Returns the lifetime in seconds for the credential to remain capable
of accepting security contexts using the specified mechanism.

Returns the lifetime in seconds for the credential to remain capable
of initiating security contexts using the specified mechanism.

Returns the remaining lifetime in seconds for a credential.

Returns the credential usage mode.

Returns the credential usage mode for a specific mechanism.

Returns a hashcode value for this GSSCredential.

============ FIELD DETAIL ===========

- Field Detail

- INITIATE_AND_ACCEPT

```java
static final int INITIATE_AND_ACCEPT
```

Credential usage flag requesting that it be usable
for both context initiation and acceptance.

**See Also:** Constant Field Values

- INITIATE_ONLY

```java
static final int INITIATE_ONLY
```

Credential usage flag requesting that it be usable
for context initiation only.

**See Also:** Constant Field Values

- ACCEPT_ONLY

```java
static final int ACCEPT_ONLY
```

Credential usage flag requesting that it be usable
for context acceptance only.

**See Also:** Constant Field Values

- DEFAULT_LIFETIME

```java
static final int DEFAULT_LIFETIME
```

A lifetime constant representing the default credential lifetime. This
value it set to 0.

**See Also:** Constant Field Values

- INDEFINITE_LIFETIME

```java
static final int INDEFINITE_LIFETIME
```

A lifetime constant representing indefinite credential lifetime.
This value must is set to the maximum integer value in Java -

Integer.MAX_VALUE

.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- dispose

```java
void dispose()
throws
GSSException
```

Releases any sensitive information that the GSSCredential object may
be containing. Applications should call this method as soon as the
credential is no longer needed to minimize the time any sensitive
information is maintained.

**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- getName

```java
GSSName
getName()
throws
GSSException
```

Retrieves the name of the entity that the credential asserts.

**Returns:** a GSSName representing the entity
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- getName

```java
GSSName
getName​(
Oid
mech)
throws
GSSException
```

Retrieves a Mechanism Name of the entity that the credential
asserts. This is equivalent to calling

canonicalize

on the value returned by
the other form of

getName

.

**Parameters:** mech

- the Oid of the mechanism for which the Mechanism Name
should be returned.
**Returns:** a GSSName representing the entity canonicalized for the
desired mechanism
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

- getRemainingLifetime

```java
int getRemainingLifetime()
throws
GSSException
```

Returns the remaining lifetime in seconds for a credential. The
remaining lifetime is the minimum lifetime amongst all of the underlying
mechanism specific credential elements.

**Returns:** the minimum remaining lifetime in seconds for this
credential. A return value of

INDEFINITE_LIFETIME

indicates that the credential does
not expire. A return value of 0 indicates that the credential is
already expired.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE
**See Also:** getRemainingInitLifetime(Oid)

,

getRemainingAcceptLifetime(Oid)

- getRemainingInitLifetime

```java
int getRemainingInitLifetime​(
Oid
mech)
throws
GSSException
```

Returns the lifetime in seconds for the credential to remain capable
of initiating security contexts using the specified mechanism. This
method queries the initiator credential element that belongs to the
specified mechanism.

**Parameters:** mech

- the Oid of the mechanism whose initiator credential element
should be queried.
**Returns:** the number of seconds remaining in the life of this credential
element. A return value of

INDEFINITE_LIFETIME

indicates that the credential element does not
expire. A return value of 0 indicates that the credential element is
already expired.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

- getRemainingAcceptLifetime

```java
int getRemainingAcceptLifetime​(
Oid
mech)
throws
GSSException
```

Returns the lifetime in seconds for the credential to remain capable
of accepting security contexts using the specified mechanism. This
method queries the acceptor credential element that belongs to the
specified mechanism.

**Parameters:** mech

- the Oid of the mechanism whose acceptor credential element
should be queried.
**Returns:** the number of seconds remaining in the life of this credential
element. A return value of

INDEFINITE_LIFETIME

indicates that the credential element does not
expire. A return value of 0 indicates that the credential element is
already expired.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

- getUsage

```java
int getUsage()
throws
GSSException
```

Returns the credential usage mode. In other words, it
tells us if this credential can be used for initiating or accepting
security contexts. It does not tell us which mechanism(s) has to be
used in order to do so. It is expected that an application will allow
the GSS-API to pick a default mechanism after calling this method.

**Returns:** The return value will be one of

INITIATE_ONLY

,

ACCEPT_ONLY

, and

INITIATE_AND_ACCEPT

.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- getUsage

```java
int getUsage​(
Oid
mech)
throws
GSSException
```

Returns the credential usage mode for a specific mechanism. In other
words, it tells us if this credential can be used
for initiating or accepting security contexts with a given underlying
mechanism.

**Parameters:** mech

- the Oid of the mechanism whose credentials usage mode is
to be determined.
**Returns:** The return value will be one of

INITIATE_ONLY

,

ACCEPT_ONLY

, and

INITIATE_AND_ACCEPT

.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

- getMechs

```java
Oid
[] getMechs()
throws
GSSException
```

Returns a list of mechanisms supported by this credential. It does
not tell us which ones can be used to initiate
contexts and which ones can be used to accept contexts. The
application must call the

getUsage

method with
each of the returned Oid's to determine the possible modes of
usage.

**Returns:** an array of Oid's corresponding to the supported mechanisms.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- add

```java
void add​(
GSSName
name,
int initLifetime,
int acceptLifetime,

Oid
mech,
int usage)
throws
GSSException
```

Adds a mechanism specific credential-element to an existing
credential. This method allows the construction of credentials, one
mechanism at a time.

This routine is envisioned to be used mainly by context acceptors
during the creation of acceptor credentials which are to be used
with a variety of clients using different security mechanisms.

This routine adds the new credential element "in-place". To add the
element in a new credential, first call

clone

to obtain a
copy of this credential, then call its

add

method.

As always, GSS-API implementations must impose a local access-control
policy on callers to prevent unauthorized callers from acquiring
credentials to which they are not entitled.

Non-default values for initLifetime and acceptLifetime cannot always
be honored by the underlying mechanisms, thus callers should be
prepared to call

getRemainingInitLifetime

and

getRemainingAcceptLifetime

on the credential.

**Parameters:** name

- the name of the principal for whom this credential is to
be acquired. Use

null

to specify the default
principal.
**Parameters:** initLifetime

- the number of seconds that the credential element
should remain valid for initiating of security contexts. Use

GSSCredential.INDEFINITE_LIFETIME

to request that the credentials have the maximum permitted lifetime
for this. Use

GSSCredential.DEFAULT_LIFETIME

to request default credential lifetime
for this.
**Parameters:** acceptLifetime

- the number of seconds that the credential
element should remain valid for accepting security contexts. Use

GSSCredential.INDEFINITE_LIFETIME

to request that the credentials have the maximum permitted lifetime
for this. Use

GSSCredential.DEFAULT_LIFETIME

to request default credential lifetime
for this.
**Parameters:** mech

- the mechanism over which the credential is to be acquired.
**Parameters:** usage

- the usage mode that this credential
element should add to the credential. The value
of this parameter must be one of:

INITIATE_AND_ACCEPT

,

ACCEPT_ONLY

, and

INITIATE_ONLY

.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.DUPLICATE_ELEMENT

,

GSSException.BAD_MECH

,

GSSException.BAD_NAMETYPE

,

GSSException.NO_CRED

,

GSSException.CREDENTIALS_EXPIRED

,

GSSException.FAILURE

- equals

```java
boolean equals​(
Object
another)
```

Tests if this GSSCredential asserts the same entity as the supplied
object. The two credentials must be acquired over the same
mechanisms and must refer to the same principal.

**Overrides:** equals

in class

Object
**Parameters:** another

- another GSSCredential for comparison to this one
**Returns:** true

if the two GSSCredentials assert the same
entity;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns a hashcode value for this GSSCredential.

**Overrides:** hashCode

in class

Object
**Returns:** a hashCode value
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Field Detail

- INITIATE_AND_ACCEPT

```java
static final int INITIATE_AND_ACCEPT
```

Credential usage flag requesting that it be usable
for both context initiation and acceptance.

**See Also:** Constant Field Values

- INITIATE_ONLY

```java
static final int INITIATE_ONLY
```

Credential usage flag requesting that it be usable
for context initiation only.

**See Also:** Constant Field Values

- ACCEPT_ONLY

```java
static final int ACCEPT_ONLY
```

Credential usage flag requesting that it be usable
for context acceptance only.

**See Also:** Constant Field Values

- DEFAULT_LIFETIME

```java
static final int DEFAULT_LIFETIME
```

A lifetime constant representing the default credential lifetime. This
value it set to 0.

**See Also:** Constant Field Values

- INDEFINITE_LIFETIME

```java
static final int INDEFINITE_LIFETIME
```

A lifetime constant representing indefinite credential lifetime.
This value must is set to the maximum integer value in Java -

Integer.MAX_VALUE

.

**See Also:** Constant Field Values

---

#### Field Detail

INITIATE_AND_ACCEPT

```java
static final int INITIATE_AND_ACCEPT
```

Credential usage flag requesting that it be usable
for both context initiation and acceptance.

**See Also:** Constant Field Values

---

#### INITIATE_AND_ACCEPT

static final int INITIATE_AND_ACCEPT

Credential usage flag requesting that it be usable
for both context initiation and acceptance.

INITIATE_ONLY

```java
static final int INITIATE_ONLY
```

Credential usage flag requesting that it be usable
for context initiation only.

**See Also:** Constant Field Values

---

#### INITIATE_ONLY

static final int INITIATE_ONLY

Credential usage flag requesting that it be usable
for context initiation only.

ACCEPT_ONLY

```java
static final int ACCEPT_ONLY
```

Credential usage flag requesting that it be usable
for context acceptance only.

**See Also:** Constant Field Values

---

#### ACCEPT_ONLY

static final int ACCEPT_ONLY

Credential usage flag requesting that it be usable
for context acceptance only.

DEFAULT_LIFETIME

```java
static final int DEFAULT_LIFETIME
```

A lifetime constant representing the default credential lifetime. This
value it set to 0.

**See Also:** Constant Field Values

---

#### DEFAULT_LIFETIME

static final int DEFAULT_LIFETIME

A lifetime constant representing the default credential lifetime. This
value it set to 0.

INDEFINITE_LIFETIME

```java
static final int INDEFINITE_LIFETIME
```

A lifetime constant representing indefinite credential lifetime.
This value must is set to the maximum integer value in Java -

Integer.MAX_VALUE

.

**See Also:** Constant Field Values

---

#### INDEFINITE_LIFETIME

static final int INDEFINITE_LIFETIME

A lifetime constant representing indefinite credential lifetime.
This value must is set to the maximum integer value in Java -

Integer.MAX_VALUE

.

Method Detail

- dispose

```java
void dispose()
throws
GSSException
```

Releases any sensitive information that the GSSCredential object may
be containing. Applications should call this method as soon as the
credential is no longer needed to minimize the time any sensitive
information is maintained.

**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- getName

```java
GSSName
getName()
throws
GSSException
```

Retrieves the name of the entity that the credential asserts.

**Returns:** a GSSName representing the entity
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- getName

```java
GSSName
getName​(
Oid
mech)
throws
GSSException
```

Retrieves a Mechanism Name of the entity that the credential
asserts. This is equivalent to calling

canonicalize

on the value returned by
the other form of

getName

.

**Parameters:** mech

- the Oid of the mechanism for which the Mechanism Name
should be returned.
**Returns:** a GSSName representing the entity canonicalized for the
desired mechanism
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

- getRemainingLifetime

```java
int getRemainingLifetime()
throws
GSSException
```

Returns the remaining lifetime in seconds for a credential. The
remaining lifetime is the minimum lifetime amongst all of the underlying
mechanism specific credential elements.

**Returns:** the minimum remaining lifetime in seconds for this
credential. A return value of

INDEFINITE_LIFETIME

indicates that the credential does
not expire. A return value of 0 indicates that the credential is
already expired.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE
**See Also:** getRemainingInitLifetime(Oid)

,

getRemainingAcceptLifetime(Oid)

- getRemainingInitLifetime

```java
int getRemainingInitLifetime​(
Oid
mech)
throws
GSSException
```

Returns the lifetime in seconds for the credential to remain capable
of initiating security contexts using the specified mechanism. This
method queries the initiator credential element that belongs to the
specified mechanism.

**Parameters:** mech

- the Oid of the mechanism whose initiator credential element
should be queried.
**Returns:** the number of seconds remaining in the life of this credential
element. A return value of

INDEFINITE_LIFETIME

indicates that the credential element does not
expire. A return value of 0 indicates that the credential element is
already expired.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

- getRemainingAcceptLifetime

```java
int getRemainingAcceptLifetime​(
Oid
mech)
throws
GSSException
```

Returns the lifetime in seconds for the credential to remain capable
of accepting security contexts using the specified mechanism. This
method queries the acceptor credential element that belongs to the
specified mechanism.

**Parameters:** mech

- the Oid of the mechanism whose acceptor credential element
should be queried.
**Returns:** the number of seconds remaining in the life of this credential
element. A return value of

INDEFINITE_LIFETIME

indicates that the credential element does not
expire. A return value of 0 indicates that the credential element is
already expired.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

- getUsage

```java
int getUsage()
throws
GSSException
```

Returns the credential usage mode. In other words, it
tells us if this credential can be used for initiating or accepting
security contexts. It does not tell us which mechanism(s) has to be
used in order to do so. It is expected that an application will allow
the GSS-API to pick a default mechanism after calling this method.

**Returns:** The return value will be one of

INITIATE_ONLY

,

ACCEPT_ONLY

, and

INITIATE_AND_ACCEPT

.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- getUsage

```java
int getUsage​(
Oid
mech)
throws
GSSException
```

Returns the credential usage mode for a specific mechanism. In other
words, it tells us if this credential can be used
for initiating or accepting security contexts with a given underlying
mechanism.

**Parameters:** mech

- the Oid of the mechanism whose credentials usage mode is
to be determined.
**Returns:** The return value will be one of

INITIATE_ONLY

,

ACCEPT_ONLY

, and

INITIATE_AND_ACCEPT

.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

- getMechs

```java
Oid
[] getMechs()
throws
GSSException
```

Returns a list of mechanisms supported by this credential. It does
not tell us which ones can be used to initiate
contexts and which ones can be used to accept contexts. The
application must call the

getUsage

method with
each of the returned Oid's to determine the possible modes of
usage.

**Returns:** an array of Oid's corresponding to the supported mechanisms.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

- add

```java
void add​(
GSSName
name,
int initLifetime,
int acceptLifetime,

Oid
mech,
int usage)
throws
GSSException
```

Adds a mechanism specific credential-element to an existing
credential. This method allows the construction of credentials, one
mechanism at a time.

This routine is envisioned to be used mainly by context acceptors
during the creation of acceptor credentials which are to be used
with a variety of clients using different security mechanisms.

This routine adds the new credential element "in-place". To add the
element in a new credential, first call

clone

to obtain a
copy of this credential, then call its

add

method.

As always, GSS-API implementations must impose a local access-control
policy on callers to prevent unauthorized callers from acquiring
credentials to which they are not entitled.

Non-default values for initLifetime and acceptLifetime cannot always
be honored by the underlying mechanisms, thus callers should be
prepared to call

getRemainingInitLifetime

and

getRemainingAcceptLifetime

on the credential.

**Parameters:** name

- the name of the principal for whom this credential is to
be acquired. Use

null

to specify the default
principal.
**Parameters:** initLifetime

- the number of seconds that the credential element
should remain valid for initiating of security contexts. Use

GSSCredential.INDEFINITE_LIFETIME

to request that the credentials have the maximum permitted lifetime
for this. Use

GSSCredential.DEFAULT_LIFETIME

to request default credential lifetime
for this.
**Parameters:** acceptLifetime

- the number of seconds that the credential
element should remain valid for accepting security contexts. Use

GSSCredential.INDEFINITE_LIFETIME

to request that the credentials have the maximum permitted lifetime
for this. Use

GSSCredential.DEFAULT_LIFETIME

to request default credential lifetime
for this.
**Parameters:** mech

- the mechanism over which the credential is to be acquired.
**Parameters:** usage

- the usage mode that this credential
element should add to the credential. The value
of this parameter must be one of:

INITIATE_AND_ACCEPT

,

ACCEPT_ONLY

, and

INITIATE_ONLY

.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.DUPLICATE_ELEMENT

,

GSSException.BAD_MECH

,

GSSException.BAD_NAMETYPE

,

GSSException.NO_CRED

,

GSSException.CREDENTIALS_EXPIRED

,

GSSException.FAILURE

- equals

```java
boolean equals​(
Object
another)
```

Tests if this GSSCredential asserts the same entity as the supplied
object. The two credentials must be acquired over the same
mechanisms and must refer to the same principal.

**Overrides:** equals

in class

Object
**Parameters:** another

- another GSSCredential for comparison to this one
**Returns:** true

if the two GSSCredentials assert the same
entity;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns a hashcode value for this GSSCredential.

**Overrides:** hashCode

in class

Object
**Returns:** a hashCode value
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

dispose

```java
void dispose()
throws
GSSException
```

Releases any sensitive information that the GSSCredential object may
be containing. Applications should call this method as soon as the
credential is no longer needed to minimize the time any sensitive
information is maintained.

**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### dispose

void dispose()
throws

GSSException

Releases any sensitive information that the GSSCredential object may
be containing. Applications should call this method as soon as the
credential is no longer needed to minimize the time any sensitive
information is maintained.

getName

```java
GSSName
getName()
throws
GSSException
```

Retrieves the name of the entity that the credential asserts.

**Returns:** a GSSName representing the entity
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### getName

GSSName

getName()
throws

GSSException

Retrieves the name of the entity that the credential asserts.

getName

```java
GSSName
getName​(
Oid
mech)
throws
GSSException
```

Retrieves a Mechanism Name of the entity that the credential
asserts. This is equivalent to calling

canonicalize

on the value returned by
the other form of

getName

.

**Parameters:** mech

- the Oid of the mechanism for which the Mechanism Name
should be returned.
**Returns:** a GSSName representing the entity canonicalized for the
desired mechanism
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

---

#### getName

GSSName

getName​(

Oid

mech)
throws

GSSException

Retrieves a Mechanism Name of the entity that the credential
asserts. This is equivalent to calling

canonicalize

on the value returned by
the other form of

getName

.

getRemainingLifetime

```java
int getRemainingLifetime()
throws
GSSException
```

Returns the remaining lifetime in seconds for a credential. The
remaining lifetime is the minimum lifetime amongst all of the underlying
mechanism specific credential elements.

**Returns:** the minimum remaining lifetime in seconds for this
credential. A return value of

INDEFINITE_LIFETIME

indicates that the credential does
not expire. A return value of 0 indicates that the credential is
already expired.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE
**See Also:** getRemainingInitLifetime(Oid)

,

getRemainingAcceptLifetime(Oid)

---

#### getRemainingLifetime

int getRemainingLifetime()
throws

GSSException

Returns the remaining lifetime in seconds for a credential. The
remaining lifetime is the minimum lifetime amongst all of the underlying
mechanism specific credential elements.

getRemainingInitLifetime

```java
int getRemainingInitLifetime​(
Oid
mech)
throws
GSSException
```

Returns the lifetime in seconds for the credential to remain capable
of initiating security contexts using the specified mechanism. This
method queries the initiator credential element that belongs to the
specified mechanism.

**Parameters:** mech

- the Oid of the mechanism whose initiator credential element
should be queried.
**Returns:** the number of seconds remaining in the life of this credential
element. A return value of

INDEFINITE_LIFETIME

indicates that the credential element does not
expire. A return value of 0 indicates that the credential element is
already expired.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

---

#### getRemainingInitLifetime

int getRemainingInitLifetime​(

Oid

mech)
throws

GSSException

Returns the lifetime in seconds for the credential to remain capable
of initiating security contexts using the specified mechanism. This
method queries the initiator credential element that belongs to the
specified mechanism.

getRemainingAcceptLifetime

```java
int getRemainingAcceptLifetime​(
Oid
mech)
throws
GSSException
```

Returns the lifetime in seconds for the credential to remain capable
of accepting security contexts using the specified mechanism. This
method queries the acceptor credential element that belongs to the
specified mechanism.

**Parameters:** mech

- the Oid of the mechanism whose acceptor credential element
should be queried.
**Returns:** the number of seconds remaining in the life of this credential
element. A return value of

INDEFINITE_LIFETIME

indicates that the credential element does not
expire. A return value of 0 indicates that the credential element is
already expired.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

---

#### getRemainingAcceptLifetime

int getRemainingAcceptLifetime​(

Oid

mech)
throws

GSSException

Returns the lifetime in seconds for the credential to remain capable
of accepting security contexts using the specified mechanism. This
method queries the acceptor credential element that belongs to the
specified mechanism.

getUsage

```java
int getUsage()
throws
GSSException
```

Returns the credential usage mode. In other words, it
tells us if this credential can be used for initiating or accepting
security contexts. It does not tell us which mechanism(s) has to be
used in order to do so. It is expected that an application will allow
the GSS-API to pick a default mechanism after calling this method.

**Returns:** The return value will be one of

INITIATE_ONLY

,

ACCEPT_ONLY

, and

INITIATE_AND_ACCEPT

.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### getUsage

int getUsage()
throws

GSSException

Returns the credential usage mode. In other words, it
tells us if this credential can be used for initiating or accepting
security contexts. It does not tell us which mechanism(s) has to be
used in order to do so. It is expected that an application will allow
the GSS-API to pick a default mechanism after calling this method.

getUsage

```java
int getUsage​(
Oid
mech)
throws
GSSException
```

Returns the credential usage mode for a specific mechanism. In other
words, it tells us if this credential can be used
for initiating or accepting security contexts with a given underlying
mechanism.

**Parameters:** mech

- the Oid of the mechanism whose credentials usage mode is
to be determined.
**Returns:** The return value will be one of

INITIATE_ONLY

,

ACCEPT_ONLY

, and

INITIATE_AND_ACCEPT

.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.BAD_MECH

,

GSSException.FAILURE

---

#### getUsage

int getUsage​(

Oid

mech)
throws

GSSException

Returns the credential usage mode for a specific mechanism. In other
words, it tells us if this credential can be used
for initiating or accepting security contexts with a given underlying
mechanism.

getMechs

```java
Oid
[] getMechs()
throws
GSSException
```

Returns a list of mechanisms supported by this credential. It does
not tell us which ones can be used to initiate
contexts and which ones can be used to accept contexts. The
application must call the

getUsage

method with
each of the returned Oid's to determine the possible modes of
usage.

**Returns:** an array of Oid's corresponding to the supported mechanisms.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.FAILURE

---

#### getMechs

Oid

[] getMechs()
throws

GSSException

Returns a list of mechanisms supported by this credential. It does
not tell us which ones can be used to initiate
contexts and which ones can be used to accept contexts. The
application must call the

getUsage

method with
each of the returned Oid's to determine the possible modes of
usage.

add

```java
void add​(
GSSName
name,
int initLifetime,
int acceptLifetime,

Oid
mech,
int usage)
throws
GSSException
```

Adds a mechanism specific credential-element to an existing
credential. This method allows the construction of credentials, one
mechanism at a time.

This routine is envisioned to be used mainly by context acceptors
during the creation of acceptor credentials which are to be used
with a variety of clients using different security mechanisms.

This routine adds the new credential element "in-place". To add the
element in a new credential, first call

clone

to obtain a
copy of this credential, then call its

add

method.

As always, GSS-API implementations must impose a local access-control
policy on callers to prevent unauthorized callers from acquiring
credentials to which they are not entitled.

Non-default values for initLifetime and acceptLifetime cannot always
be honored by the underlying mechanisms, thus callers should be
prepared to call

getRemainingInitLifetime

and

getRemainingAcceptLifetime

on the credential.

**Parameters:** name

- the name of the principal for whom this credential is to
be acquired. Use

null

to specify the default
principal.
**Parameters:** initLifetime

- the number of seconds that the credential element
should remain valid for initiating of security contexts. Use

GSSCredential.INDEFINITE_LIFETIME

to request that the credentials have the maximum permitted lifetime
for this. Use

GSSCredential.DEFAULT_LIFETIME

to request default credential lifetime
for this.
**Parameters:** acceptLifetime

- the number of seconds that the credential
element should remain valid for accepting security contexts. Use

GSSCredential.INDEFINITE_LIFETIME

to request that the credentials have the maximum permitted lifetime
for this. Use

GSSCredential.DEFAULT_LIFETIME

to request default credential lifetime
for this.
**Parameters:** mech

- the mechanism over which the credential is to be acquired.
**Parameters:** usage

- the usage mode that this credential
element should add to the credential. The value
of this parameter must be one of:

INITIATE_AND_ACCEPT

,

ACCEPT_ONLY

, and

INITIATE_ONLY

.
**Throws:** GSSException

- containing the following
major error codes:

GSSException.DUPLICATE_ELEMENT

,

GSSException.BAD_MECH

,

GSSException.BAD_NAMETYPE

,

GSSException.NO_CRED

,

GSSException.CREDENTIALS_EXPIRED

,

GSSException.FAILURE

---

#### add

void add​(

GSSName

name,
int initLifetime,
int acceptLifetime,

Oid

mech,
int usage)
throws

GSSException

Adds a mechanism specific credential-element to an existing
credential. This method allows the construction of credentials, one
mechanism at a time.

This routine is envisioned to be used mainly by context acceptors
during the creation of acceptor credentials which are to be used
with a variety of clients using different security mechanisms.

This routine adds the new credential element "in-place". To add the
element in a new credential, first call

clone

to obtain a
copy of this credential, then call its

add

method.

As always, GSS-API implementations must impose a local access-control
policy on callers to prevent unauthorized callers from acquiring
credentials to which they are not entitled.

Non-default values for initLifetime and acceptLifetime cannot always
be honored by the underlying mechanisms, thus callers should be
prepared to call

getRemainingInitLifetime

and

getRemainingAcceptLifetime

on the credential.

This routine is envisioned to be used mainly by context acceptors
during the creation of acceptor credentials which are to be used
with a variety of clients using different security mechanisms.

This routine adds the new credential element "in-place". To add the
element in a new credential, first call

clone

to obtain a
copy of this credential, then call its

add

method.

As always, GSS-API implementations must impose a local access-control
policy on callers to prevent unauthorized callers from acquiring
credentials to which they are not entitled.

Non-default values for initLifetime and acceptLifetime cannot always
be honored by the underlying mechanisms, thus callers should be
prepared to call

getRemainingInitLifetime

and

getRemainingAcceptLifetime

on the credential.

This routine adds the new credential element "in-place". To add the
element in a new credential, first call

clone

to obtain a
copy of this credential, then call its

add

method.

As always, GSS-API implementations must impose a local access-control
policy on callers to prevent unauthorized callers from acquiring
credentials to which they are not entitled.

Non-default values for initLifetime and acceptLifetime cannot always
be honored by the underlying mechanisms, thus callers should be
prepared to call

getRemainingInitLifetime

and

getRemainingAcceptLifetime

on the credential.

As always, GSS-API implementations must impose a local access-control
policy on callers to prevent unauthorized callers from acquiring
credentials to which they are not entitled.

Non-default values for initLifetime and acceptLifetime cannot always
be honored by the underlying mechanisms, thus callers should be
prepared to call

getRemainingInitLifetime

and

getRemainingAcceptLifetime

on the credential.

equals

```java
boolean equals​(
Object
another)
```

Tests if this GSSCredential asserts the same entity as the supplied
object. The two credentials must be acquired over the same
mechanisms and must refer to the same principal.

**Overrides:** equals

in class

Object
**Parameters:** another

- another GSSCredential for comparison to this one
**Returns:** true

if the two GSSCredentials assert the same
entity;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

another)

Tests if this GSSCredential asserts the same entity as the supplied
object. The two credentials must be acquired over the same
mechanisms and must refer to the same principal.

hashCode

```java
int hashCode()
```

Returns a hashcode value for this GSSCredential.

**Overrides:** hashCode

in class

Object
**Returns:** a hashCode value
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns a hashcode value for this GSSCredential.

---

