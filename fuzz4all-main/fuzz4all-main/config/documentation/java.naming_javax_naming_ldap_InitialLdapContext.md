# Class InitialLdapContext

**Source:** `java.naming\javax\naming\ldap\InitialLdapContext.html`

### Class Description

```java
public class
InitialLdapContext

extends
InitialDirContext

implements
LdapContext
```

This class is the starting context for performing
LDAPv3-style extended operations and controls.

See

javax.naming.InitialContext

and

javax.naming.InitialDirContext

for details on synchronization,
and the policy for how an initial context is created.

Request Controls

When you create an initial context (

InitialLdapContext

),
you can specify a list of request controls.
These controls will be used as the request controls for any
implicit LDAP "bind" operation performed by the context or contexts
derived from the context. These are called

connection request controls

.
Use

getConnectControls()

to get a context's connection request
controls.

The request controls supplied to the initial context constructor
are

not

used as the context request controls
for subsequent context operations such as searches and lookups.
Context request controls are set and updated by using

setRequestControls()

.

As shown, there can be two different sets of request controls
associated with a context: connection request controls and context
request controls.
This is required for those applications needing to send critical
controls that might not be applicable to both the context operation and
any implicit LDAP "bind" operation.
A typical user program would do the following:

```java
InitialLdapContext lctx = new InitialLdapContext(env, critConnCtls);
lctx.setRequestControls(critModCtls);
lctx.modifyAttributes(name, mods);
Controls[] respCtls = lctx.getResponseControls();
```

It specifies first the critical controls for creating the initial context
(

critConnCtls

), and then sets the context's request controls
(

critModCtls

) for the context operation. If for some reason

lctx

needs to reconnect to the server, it will use

critConnCtls

. See the

LdapContext

interface for
more discussion about request controls.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

**All Implemented Interfaces:** Context

,

DirContext

,

LdapContext

---

### Field Details

*No entries found.*

### Constructor Details

#### public InitialLdapContext()
throws
NamingException

Constructs an initial context using no environment properties or
connection request controls.
Equivalent to

new InitialLdapContext(null, null)

.

**Throws:**
- NamingException

- if a naming exception is encountered

---

#### public InitialLdapContext​(
Hashtable
<?,​?> environment,

Control
[] connCtls)
throws
NamingException

Constructs an initial context
using environment properties and connection request controls.
See

javax.naming.InitialContext

for a discussion of
environment properties.

This constructor will not modify its parameters or
save references to them, but may save a clone or copy.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

connCtls

is used as the underlying context instance's
connection request controls. See the class description
for details.

**Parameters:**
- environment

- environment used to create the initial DirContext.
Null indicates an empty environment.
- connCtls

- connection request controls for the initial context.
If null, no connection request controls are used.

**Throws:**
- NamingException

- if a naming exception is encountered

**See Also:**
- LdapContext.reconnect(javax.naming.ldap.Control[])

,

LdapContext.reconnect(javax.naming.ldap.Control[])

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InitialLdapContext

java.lang.Object

- javax.naming.InitialContext
- - javax.naming.directory.InitialDirContext
- - javax.naming.ldap.InitialLdapContext

javax.naming.InitialContext

- javax.naming.directory.InitialDirContext
- - javax.naming.ldap.InitialLdapContext

javax.naming.directory.InitialDirContext

- javax.naming.ldap.InitialLdapContext

javax.naming.ldap.InitialLdapContext

**All Implemented Interfaces:** Context

,

DirContext

,

LdapContext

```java
public class
InitialLdapContext

extends
InitialDirContext

implements
LdapContext
```

This class is the starting context for performing
LDAPv3-style extended operations and controls.

See

javax.naming.InitialContext

and

javax.naming.InitialDirContext

for details on synchronization,
and the policy for how an initial context is created.

Request Controls

When you create an initial context (

InitialLdapContext

),
you can specify a list of request controls.
These controls will be used as the request controls for any
implicit LDAP "bind" operation performed by the context or contexts
derived from the context. These are called

connection request controls

.
Use

getConnectControls()

to get a context's connection request
controls.

The request controls supplied to the initial context constructor
are

not

used as the context request controls
for subsequent context operations such as searches and lookups.
Context request controls are set and updated by using

setRequestControls()

.

As shown, there can be two different sets of request controls
associated with a context: connection request controls and context
request controls.
This is required for those applications needing to send critical
controls that might not be applicable to both the context operation and
any implicit LDAP "bind" operation.
A typical user program would do the following:

```java
InitialLdapContext lctx = new InitialLdapContext(env, critConnCtls);
lctx.setRequestControls(critModCtls);
lctx.modifyAttributes(name, mods);
Controls[] respCtls = lctx.getResponseControls();
```

It specifies first the critical controls for creating the initial context
(

critConnCtls

), and then sets the context's request controls
(

critModCtls

) for the context operation. If for some reason

lctx

needs to reconnect to the server, it will use

critConnCtls

. See the

LdapContext

interface for
more discussion about request controls.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

**Since:** 1.3
**See Also:** LdapContext

,

InitialContext

,

InitialDirContext

,

NamingManager.setInitialContextFactoryBuilder(javax.naming.spi.InitialContextFactoryBuilder)

public class

InitialLdapContext

extends

InitialDirContext

implements

LdapContext

This class is the starting context for performing
LDAPv3-style extended operations and controls.

See

javax.naming.InitialContext

and

javax.naming.InitialDirContext

for details on synchronization,
and the policy for how an initial context is created.

Request Controls

When you create an initial context (

InitialLdapContext

),
you can specify a list of request controls.
These controls will be used as the request controls for any
implicit LDAP "bind" operation performed by the context or contexts
derived from the context. These are called

connection request controls

.
Use

getConnectControls()

to get a context's connection request
controls.

The request controls supplied to the initial context constructor
are

not

used as the context request controls
for subsequent context operations such as searches and lookups.
Context request controls are set and updated by using

setRequestControls()

.

As shown, there can be two different sets of request controls
associated with a context: connection request controls and context
request controls.
This is required for those applications needing to send critical
controls that might not be applicable to both the context operation and
any implicit LDAP "bind" operation.
A typical user program would do the following:

```java
InitialLdapContext lctx = new InitialLdapContext(env, critConnCtls);
lctx.setRequestControls(critModCtls);
lctx.modifyAttributes(name, mods);
Controls[] respCtls = lctx.getResponseControls();
```

It specifies first the critical controls for creating the initial context
(

critConnCtls

), and then sets the context's request controls
(

critModCtls

) for the context operation. If for some reason

lctx

needs to reconnect to the server, it will use

critConnCtls

. See the

LdapContext

interface for
more discussion about request controls.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

See

javax.naming.InitialContext

and

javax.naming.InitialDirContext

for details on synchronization,
and the policy for how an initial context is created.

Request Controls

When you create an initial context (

InitialLdapContext

),
you can specify a list of request controls.
These controls will be used as the request controls for any
implicit LDAP "bind" operation performed by the context or contexts
derived from the context. These are called

connection request controls

.
Use

getConnectControls()

to get a context's connection request
controls.

The request controls supplied to the initial context constructor
are

not

used as the context request controls
for subsequent context operations such as searches and lookups.
Context request controls are set and updated by using

setRequestControls()

.

As shown, there can be two different sets of request controls
associated with a context: connection request controls and context
request controls.
This is required for those applications needing to send critical
controls that might not be applicable to both the context operation and
any implicit LDAP "bind" operation.
A typical user program would do the following:

```java
InitialLdapContext lctx = new InitialLdapContext(env, critConnCtls);
lctx.setRequestControls(critModCtls);
lctx.modifyAttributes(name, mods);
Controls[] respCtls = lctx.getResponseControls();
```

It specifies first the critical controls for creating the initial context
(

critConnCtls

), and then sets the context's request controls
(

critModCtls

) for the context operation. If for some reason

lctx

needs to reconnect to the server, it will use

critConnCtls

. See the

LdapContext

interface for
more discussion about request controls.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

---

#### Request Controls

The request controls supplied to the initial context constructor
are

not

used as the context request controls
for subsequent context operations such as searches and lookups.
Context request controls are set and updated by using

setRequestControls()

.

As shown, there can be two different sets of request controls
associated with a context: connection request controls and context
request controls.
This is required for those applications needing to send critical
controls that might not be applicable to both the context operation and
any implicit LDAP "bind" operation.
A typical user program would do the following:

```java
InitialLdapContext lctx = new InitialLdapContext(env, critConnCtls);
lctx.setRequestControls(critModCtls);
lctx.modifyAttributes(name, mods);
Controls[] respCtls = lctx.getResponseControls();
```

It specifies first the critical controls for creating the initial context
(

critConnCtls

), and then sets the context's request controls
(

critModCtls

) for the context operation. If for some reason

lctx

needs to reconnect to the server, it will use

critConnCtls

. See the

LdapContext

interface for
more discussion about request controls.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

As shown, there can be two different sets of request controls
associated with a context: connection request controls and context
request controls.
This is required for those applications needing to send critical
controls that might not be applicable to both the context operation and
any implicit LDAP "bind" operation.
A typical user program would do the following:

```java
InitialLdapContext lctx = new InitialLdapContext(env, critConnCtls);
lctx.setRequestControls(critModCtls);
lctx.modifyAttributes(name, mods);
Controls[] respCtls = lctx.getResponseControls();
```

It specifies first the critical controls for creating the initial context
(

critConnCtls

), and then sets the context's request controls
(

critModCtls

) for the context operation. If for some reason

lctx

needs to reconnect to the server, it will use

critConnCtls

. See the

LdapContext

interface for
more discussion about request controls.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

InitialLdapContext lctx = new InitialLdapContext(env, critConnCtls);
lctx.setRequestControls(critModCtls);
lctx.modifyAttributes(name, mods);
Controls[] respCtls = lctx.getResponseControls();

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.naming.

InitialContext

defaultInitCtx

,

gotDefault

,

myProps

- Fields declared in interface javax.naming.

Context

APPLET

,

AUTHORITATIVE

,

BATCHSIZE

,

DNS_URL

,

INITIAL_CONTEXT_FACTORY

,

LANGUAGE

,

OBJECT_FACTORIES

,

PROVIDER_URL

,

REFERRAL

,

SECURITY_AUTHENTICATION

,

SECURITY_CREDENTIALS

,

SECURITY_PRINCIPAL

,

SECURITY_PROTOCOL

,

STATE_FACTORIES

,

URL_PKG_PREFIXES

- Fields declared in interface javax.naming.directory.

DirContext

ADD_ATTRIBUTE

,

REMOVE_ATTRIBUTE

,

REPLACE_ATTRIBUTE

- Fields declared in interface javax.naming.ldap.

LdapContext

CONTROL_FACTORIES

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InitialLdapContext

()

Constructs an initial context using no environment properties or
connection request controls.

InitialLdapContext

​(

Hashtable

<?,​?> environment,

Control

[] connCtls)

Constructs an initial context
using environment properties and connection request controls.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.naming.

InitialContext

composeName

,

composeName

,

doLookup

,

doLookup

,

getDefaultInitCtx

,

getURLOrDefaultInitCtx

,

getURLOrDefaultInitCtx

,

init

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

- Methods declared in interface javax.naming.

Context

addToEnvironment

,

bind

,

bind

,

close

,

composeName

,

composeName

,

createSubcontext

,

createSubcontext

,

destroySubcontext

,

destroySubcontext

,

getEnvironment

,

getNameInNamespace

,

getNameParser

,

getNameParser

,

list

,

list

,

listBindings

,

listBindings

,

lookup

,

lookup

,

lookupLink

,

lookupLink

,

rebind

,

rebind

,

removeFromEnvironment

,

rename

,

rename

,

unbind

,

unbind

- Methods declared in interface javax.naming.directory.

DirContext

bind

,

bind

,

createSubcontext

,

createSubcontext

,

getAttributes

,

getAttributes

,

getAttributes

,

getAttributes

,

getSchema

,

getSchema

,

getSchemaClassDefinition

,

getSchemaClassDefinition

,

modifyAttributes

,

modifyAttributes

,

modifyAttributes

,

modifyAttributes

,

rebind

,

rebind

,

search

,

search

,

search

,

search

,

search

,

search

,

search

,

search

- Methods declared in interface javax.naming.ldap.

LdapContext

extendedOperation

,

getConnectControls

,

getRequestControls

,

getResponseControls

,

newInstance

,

reconnect

,

setRequestControls

Field Summary

- Fields declared in class javax.naming.

InitialContext

defaultInitCtx

,

gotDefault

,

myProps

- Fields declared in interface javax.naming.

Context

APPLET

,

AUTHORITATIVE

,

BATCHSIZE

,

DNS_URL

,

INITIAL_CONTEXT_FACTORY

,

LANGUAGE

,

OBJECT_FACTORIES

,

PROVIDER_URL

,

REFERRAL

,

SECURITY_AUTHENTICATION

,

SECURITY_CREDENTIALS

,

SECURITY_PRINCIPAL

,

SECURITY_PROTOCOL

,

STATE_FACTORIES

,

URL_PKG_PREFIXES

- Fields declared in interface javax.naming.directory.

DirContext

ADD_ATTRIBUTE

,

REMOVE_ATTRIBUTE

,

REPLACE_ATTRIBUTE

- Fields declared in interface javax.naming.ldap.

LdapContext

CONTROL_FACTORIES

---

#### Field Summary

Fields declared in class javax.naming.

InitialContext

defaultInitCtx

,

gotDefault

,

myProps

---

#### Fields declared in class javax.naming. InitialContext

Fields declared in interface javax.naming.

Context

APPLET

,

AUTHORITATIVE

,

BATCHSIZE

,

DNS_URL

,

INITIAL_CONTEXT_FACTORY

,

LANGUAGE

,

OBJECT_FACTORIES

,

PROVIDER_URL

,

REFERRAL

,

SECURITY_AUTHENTICATION

,

SECURITY_CREDENTIALS

,

SECURITY_PRINCIPAL

,

SECURITY_PROTOCOL

,

STATE_FACTORIES

,

URL_PKG_PREFIXES

---

#### Fields declared in interface javax.naming. Context

Fields declared in interface javax.naming.directory.

DirContext

ADD_ATTRIBUTE

,

REMOVE_ATTRIBUTE

,

REPLACE_ATTRIBUTE

---

#### Fields declared in interface javax.naming.directory. DirContext

Fields declared in interface javax.naming.ldap.

LdapContext

CONTROL_FACTORIES

---

#### Fields declared in interface javax.naming.ldap. LdapContext

Constructor Summary

Constructors

Constructor

Description

InitialLdapContext

()

Constructs an initial context using no environment properties or
connection request controls.

InitialLdapContext

​(

Hashtable

<?,​?> environment,

Control

[] connCtls)

Constructs an initial context
using environment properties and connection request controls.

---

#### Constructor Summary

Constructs an initial context using no environment properties or
connection request controls.

Constructs an initial context
using environment properties and connection request controls.

Method Summary

- Methods declared in class javax.naming.

InitialContext

composeName

,

composeName

,

doLookup

,

doLookup

,

getDefaultInitCtx

,

getURLOrDefaultInitCtx

,

getURLOrDefaultInitCtx

,

init

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

- Methods declared in interface javax.naming.

Context

addToEnvironment

,

bind

,

bind

,

close

,

composeName

,

composeName

,

createSubcontext

,

createSubcontext

,

destroySubcontext

,

destroySubcontext

,

getEnvironment

,

getNameInNamespace

,

getNameParser

,

getNameParser

,

list

,

list

,

listBindings

,

listBindings

,

lookup

,

lookup

,

lookupLink

,

lookupLink

,

rebind

,

rebind

,

removeFromEnvironment

,

rename

,

rename

,

unbind

,

unbind

- Methods declared in interface javax.naming.directory.

DirContext

bind

,

bind

,

createSubcontext

,

createSubcontext

,

getAttributes

,

getAttributes

,

getAttributes

,

getAttributes

,

getSchema

,

getSchema

,

getSchemaClassDefinition

,

getSchemaClassDefinition

,

modifyAttributes

,

modifyAttributes

,

modifyAttributes

,

modifyAttributes

,

rebind

,

rebind

,

search

,

search

,

search

,

search

,

search

,

search

,

search

,

search

- Methods declared in interface javax.naming.ldap.

LdapContext

extendedOperation

,

getConnectControls

,

getRequestControls

,

getResponseControls

,

newInstance

,

reconnect

,

setRequestControls

---

#### Method Summary

Methods declared in class javax.naming.

InitialContext

composeName

,

composeName

,

doLookup

,

doLookup

,

getDefaultInitCtx

,

getURLOrDefaultInitCtx

,

getURLOrDefaultInitCtx

,

init

---

#### Methods declared in class javax.naming. InitialContext

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

Methods declared in interface javax.naming.

Context

addToEnvironment

,

bind

,

bind

,

close

,

composeName

,

composeName

,

createSubcontext

,

createSubcontext

,

destroySubcontext

,

destroySubcontext

,

getEnvironment

,

getNameInNamespace

,

getNameParser

,

getNameParser

,

list

,

list

,

listBindings

,

listBindings

,

lookup

,

lookup

,

lookupLink

,

lookupLink

,

rebind

,

rebind

,

removeFromEnvironment

,

rename

,

rename

,

unbind

,

unbind

---

#### Methods declared in interface javax.naming. Context

Methods declared in interface javax.naming.directory.

DirContext

bind

,

bind

,

createSubcontext

,

createSubcontext

,

getAttributes

,

getAttributes

,

getAttributes

,

getAttributes

,

getSchema

,

getSchema

,

getSchemaClassDefinition

,

getSchemaClassDefinition

,

modifyAttributes

,

modifyAttributes

,

modifyAttributes

,

modifyAttributes

,

rebind

,

rebind

,

search

,

search

,

search

,

search

,

search

,

search

,

search

,

search

---

#### Methods declared in interface javax.naming.directory. DirContext

Methods declared in interface javax.naming.ldap.

LdapContext

extendedOperation

,

getConnectControls

,

getRequestControls

,

getResponseControls

,

newInstance

,

reconnect

,

setRequestControls

---

#### Methods declared in interface javax.naming.ldap. LdapContext

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InitialLdapContext

```java
public InitialLdapContext()
throws
NamingException
```

Constructs an initial context using no environment properties or
connection request controls.
Equivalent to

new InitialLdapContext(null, null)

.

**Throws:** NamingException

- if a naming exception is encountered

- InitialLdapContext

```java
public InitialLdapContext​(
Hashtable
<?,​?> environment,

Control
[] connCtls)
throws
NamingException
```

Constructs an initial context
using environment properties and connection request controls.
See

javax.naming.InitialContext

for a discussion of
environment properties.

This constructor will not modify its parameters or
save references to them, but may save a clone or copy.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

connCtls

is used as the underlying context instance's
connection request controls. See the class description
for details.

**Parameters:** environment

- environment used to create the initial DirContext.
Null indicates an empty environment.
**Parameters:** connCtls

- connection request controls for the initial context.
If null, no connection request controls are used.
**Throws:** NamingException

- if a naming exception is encountered
**See Also:** LdapContext.reconnect(javax.naming.ldap.Control[])

,

LdapContext.reconnect(javax.naming.ldap.Control[])

Constructor Detail

- InitialLdapContext

```java
public InitialLdapContext()
throws
NamingException
```

Constructs an initial context using no environment properties or
connection request controls.
Equivalent to

new InitialLdapContext(null, null)

.

**Throws:** NamingException

- if a naming exception is encountered

- InitialLdapContext

```java
public InitialLdapContext​(
Hashtable
<?,​?> environment,

Control
[] connCtls)
throws
NamingException
```

Constructs an initial context
using environment properties and connection request controls.
See

javax.naming.InitialContext

for a discussion of
environment properties.

This constructor will not modify its parameters or
save references to them, but may save a clone or copy.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

connCtls

is used as the underlying context instance's
connection request controls. See the class description
for details.

**Parameters:** environment

- environment used to create the initial DirContext.
Null indicates an empty environment.
**Parameters:** connCtls

- connection request controls for the initial context.
If null, no connection request controls are used.
**Throws:** NamingException

- if a naming exception is encountered
**See Also:** LdapContext.reconnect(javax.naming.ldap.Control[])

,

LdapContext.reconnect(javax.naming.ldap.Control[])

---

#### Constructor Detail

InitialLdapContext

```java
public InitialLdapContext()
throws
NamingException
```

Constructs an initial context using no environment properties or
connection request controls.
Equivalent to

new InitialLdapContext(null, null)

.

**Throws:** NamingException

- if a naming exception is encountered

---

#### InitialLdapContext

public InitialLdapContext()
throws

NamingException

Constructs an initial context using no environment properties or
connection request controls.
Equivalent to

new InitialLdapContext(null, null)

.

InitialLdapContext

```java
public InitialLdapContext​(
Hashtable
<?,​?> environment,

Control
[] connCtls)
throws
NamingException
```

Constructs an initial context
using environment properties and connection request controls.
See

javax.naming.InitialContext

for a discussion of
environment properties.

This constructor will not modify its parameters or
save references to them, but may save a clone or copy.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

connCtls

is used as the underlying context instance's
connection request controls. See the class description
for details.

**Parameters:** environment

- environment used to create the initial DirContext.
Null indicates an empty environment.
**Parameters:** connCtls

- connection request controls for the initial context.
If null, no connection request controls are used.
**Throws:** NamingException

- if a naming exception is encountered
**See Also:** LdapContext.reconnect(javax.naming.ldap.Control[])

,

LdapContext.reconnect(javax.naming.ldap.Control[])

---

#### InitialLdapContext

public InitialLdapContext​(

Hashtable

<?,​?> environment,

Control

[] connCtls)
throws

NamingException

Constructs an initial context
using environment properties and connection request controls.
See

javax.naming.InitialContext

for a discussion of
environment properties.

This constructor will not modify its parameters or
save references to them, but may save a clone or copy.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

connCtls

is used as the underlying context instance's
connection request controls. See the class description
for details.

This constructor will not modify its parameters or
save references to them, but may save a clone or copy.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

connCtls

is used as the underlying context instance's
connection request controls. See the class description
for details.

connCtls

is used as the underlying context instance's
connection request controls. See the class description
for details.

---

