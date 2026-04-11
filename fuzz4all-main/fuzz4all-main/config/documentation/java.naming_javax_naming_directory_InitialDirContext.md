# Class InitialDirContext

**Source:** `java.naming\javax\naming\directory\InitialDirContext.html`

### Class Description

```java
public class
InitialDirContext

extends
InitialContext

implements
DirContext
```

This class is the starting context for performing
directory operations. The documentation in the class description
of InitialContext (including those for synchronization) apply here.

**All Implemented Interfaces:** Context

,

DirContext

---

### Field Details

*No entries found.*

### Constructor Details

#### protected InitialDirContext​(boolean lazy)
throws
NamingException

Constructs an initial DirContext with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialDirContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

**Parameters:**
- lazy

- true means do not initialize the initial DirContext; false
is equivalent to calling

new InitialDirContext()

**Throws:**
- NamingException

- if a naming exception is encountered

**See Also:**
- InitialContext.init(Hashtable)

**Since:**
- 1.3

---

#### public InitialDirContext()
throws
NamingException

Constructs an initial DirContext.
No environment properties are supplied.
Equivalent to

new InitialDirContext(null)

.

**Throws:**
- NamingException

- if a naming exception is encountered

**See Also:**
- InitialDirContext(Hashtable)

---

#### public InitialDirContext​(
Hashtable
<?,​?> environment)
throws
NamingException

Constructs an initial DirContext using the supplied environment.
Environment properties are discussed in the

javax.naming.InitialContext

class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

**Parameters:**
- environment

- environment used to create the initial DirContext.
Null indicates an empty environment.

**Throws:**
- NamingException

- if a naming exception is encountered

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InitialDirContext

java.lang.Object

- javax.naming.InitialContext
- - javax.naming.directory.InitialDirContext

javax.naming.InitialContext

- javax.naming.directory.InitialDirContext

javax.naming.directory.InitialDirContext

**All Implemented Interfaces:** Context

,

DirContext

**Direct Known Subclasses:** InitialLdapContext

```java
public class
InitialDirContext

extends
InitialContext

implements
DirContext
```

This class is the starting context for performing
directory operations. The documentation in the class description
of InitialContext (including those for synchronization) apply here.

**Since:** 1.3
**See Also:** InitialContext

public class

InitialDirContext

extends

InitialContext

implements

DirContext

This class is the starting context for performing
directory operations. The documentation in the class description
of InitialContext (including those for synchronization) apply here.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

InitialDirContext

()

Constructs an initial DirContext.

protected

InitialDirContext

​(boolean lazy)

Constructs an initial DirContext with the option of not
initializing it.

InitialDirContext

​(

Hashtable

<?,​?> environment)

Constructs an initial DirContext using the supplied environment.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

InitialDirContext

()

Constructs an initial DirContext.

protected

InitialDirContext

​(boolean lazy)

Constructs an initial DirContext with the option of not
initializing it.

InitialDirContext

​(

Hashtable

<?,​?> environment)

Constructs an initial DirContext using the supplied environment.

---

#### Constructor Summary

Constructs an initial DirContext.

Constructs an initial DirContext with the option of not
initializing it.

Constructs an initial DirContext using the supplied environment.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InitialDirContext

```java
protected InitialDirContext​(boolean lazy)
throws
NamingException
```

Constructs an initial DirContext with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialDirContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

**Parameters:** lazy

- true means do not initialize the initial DirContext; false
is equivalent to calling

new InitialDirContext()
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.3
**See Also:** InitialContext.init(Hashtable)

- InitialDirContext

```java
public InitialDirContext()
throws
NamingException
```

Constructs an initial DirContext.
No environment properties are supplied.
Equivalent to

new InitialDirContext(null)

.

**Throws:** NamingException

- if a naming exception is encountered
**See Also:** InitialDirContext(Hashtable)

- InitialDirContext

```java
public InitialDirContext​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Constructs an initial DirContext using the supplied environment.
Environment properties are discussed in the

javax.naming.InitialContext

class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

**Parameters:** environment

- environment used to create the initial DirContext.
Null indicates an empty environment.
**Throws:** NamingException

- if a naming exception is encountered

Constructor Detail

- InitialDirContext

```java
protected InitialDirContext​(boolean lazy)
throws
NamingException
```

Constructs an initial DirContext with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialDirContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

**Parameters:** lazy

- true means do not initialize the initial DirContext; false
is equivalent to calling

new InitialDirContext()
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.3
**See Also:** InitialContext.init(Hashtable)

- InitialDirContext

```java
public InitialDirContext()
throws
NamingException
```

Constructs an initial DirContext.
No environment properties are supplied.
Equivalent to

new InitialDirContext(null)

.

**Throws:** NamingException

- if a naming exception is encountered
**See Also:** InitialDirContext(Hashtable)

- InitialDirContext

```java
public InitialDirContext​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Constructs an initial DirContext using the supplied environment.
Environment properties are discussed in the

javax.naming.InitialContext

class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

**Parameters:** environment

- environment used to create the initial DirContext.
Null indicates an empty environment.
**Throws:** NamingException

- if a naming exception is encountered

---

#### Constructor Detail

InitialDirContext

```java
protected InitialDirContext​(boolean lazy)
throws
NamingException
```

Constructs an initial DirContext with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialDirContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

**Parameters:** lazy

- true means do not initialize the initial DirContext; false
is equivalent to calling

new InitialDirContext()
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.3
**See Also:** InitialContext.init(Hashtable)

---

#### InitialDirContext

protected InitialDirContext​(boolean lazy)
throws

NamingException

Constructs an initial DirContext with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialDirContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

InitialDirContext

```java
public InitialDirContext()
throws
NamingException
```

Constructs an initial DirContext.
No environment properties are supplied.
Equivalent to

new InitialDirContext(null)

.

**Throws:** NamingException

- if a naming exception is encountered
**See Also:** InitialDirContext(Hashtable)

---

#### InitialDirContext

public InitialDirContext()
throws

NamingException

Constructs an initial DirContext.
No environment properties are supplied.
Equivalent to

new InitialDirContext(null)

.

InitialDirContext

```java
public InitialDirContext​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Constructs an initial DirContext using the supplied environment.
Environment properties are discussed in the

javax.naming.InitialContext

class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

**Parameters:** environment

- environment used to create the initial DirContext.
Null indicates an empty environment.
**Throws:** NamingException

- if a naming exception is encountered

---

#### InitialDirContext

public InitialDirContext​(

Hashtable

<?,​?> environment)
throws

NamingException

Constructs an initial DirContext using the supplied environment.
Environment properties are discussed in the

javax.naming.InitialContext

class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

---

