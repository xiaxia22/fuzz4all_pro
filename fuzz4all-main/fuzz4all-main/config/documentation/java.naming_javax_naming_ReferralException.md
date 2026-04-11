# Class ReferralException

**Source:** `java.naming\javax\naming\ReferralException.html`

### Class Description

```java
public abstract class
ReferralException

extends
NamingException
```

This abstract class is used to represent a referral exception,
which is generated in response to a

referral

such as that returned by LDAP v3 servers.

A service provider provides
a subclass of

ReferralException

by providing implementations
for

getReferralInfo()

and

getReferralContext()

(and appropriate
constructors and/or corresponding "set" methods).

The following code sample shows how

ReferralException

can be used.

```java
while (true) {
try {
bindings = ctx.listBindings(name);
while (bindings.hasMore()) {
b = bindings.next();
...
}
break;
} catch (ReferralException e) {
ctx = e.getReferralContext();
}
}
```

ReferralException

is an abstract class. Concrete implementations
determine its synchronization and serialization properties.

An environment parameter passed to the

getReferralContext()

method is owned by the caller.
The service provider will not modify the object or keep a reference to it,
but may keep a reference to a clone of it.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ReferralException​(
String
explanation)

Constructs a new instance of ReferralException using the
explanation supplied. All other fields are set to null.

**Parameters:**
- explanation

- Additional detail about this exception. Can be null.

**See Also:**
- Throwable.getMessage()

---

#### protected ReferralException()

Constructs a new instance of ReferralException.
All fields are set to null.

---

### Method Details

#### public abstract
Object
getReferralInfo()

Retrieves information (such as URLs) related to this referral.
The program may examine or display this information
to the user to determine whether to continue with the referral,
or to determine additional information needs to be supplied in order
to continue with the referral.

**Returns:**
- Non-null referral information related to this referral.

---

#### public abstract
Context
getReferralContext()
throws
NamingException

Retrieves the context at which to continue the method.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation. The referral context is
created using the environment properties of the context
that threw the ReferralException.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

**Returns:**
- The non-null context at which to continue the method.

**Throws:**
- NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

---

#### public abstract
Context
getReferralContext​(
Hashtable
<?,​?> env)
throws
NamingException

Retrieves the context at which to continue the method using
environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.

The referral context is created using

env

as its environment
properties.
This method should be used instead of the no-arg overloaded form
when the caller needs to use different environment properties for
the referral context. It might need to do this, for example, when
it needs to supply different authentication information to the referred
server in order to create the referral context.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

**Parameters:**
- env

- The possibly null environment to use when retrieving the
referral context. If null, no environment properties will be used.

**Returns:**
- The non-null context at which to continue the method.

**Throws:**
- NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

---

#### public abstract boolean skipReferral()

Discards the referral about to be processed.
A call to this method should be followed by a call to

getReferralContext

to allow the processing of
other referrals to continue.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
if (!shallIFollow(e.getReferralInfo())) {
if (!e.skipReferral()) {
return;
}
}
ctx = e.getReferralContext();
}
```

**Returns:**
- true If more referral processing is pending; false otherwise.

---

#### public abstract void retryReferral()

Retries the referral currently being processed.
A call to this method should be followed by a call to

getReferralContext

to allow the current
referral to be retried.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
while (true) {
try {
ctx = e.getReferralContext(env);
break;
} catch (NamingException ne) {
if (! shallIRetry()) {
return;
}
// modify environment properties (env), if necessary
e.retryReferral();
}
}
}
```

---

### Additional Sections

#### Class ReferralException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ReferralException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ReferralException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.ReferralException

javax.naming.NamingException

- javax.naming.ReferralException

javax.naming.ReferralException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** LdapReferralException

```java
public abstract class
ReferralException

extends
NamingException
```

This abstract class is used to represent a referral exception,
which is generated in response to a

referral

such as that returned by LDAP v3 servers.

A service provider provides
a subclass of

ReferralException

by providing implementations
for

getReferralInfo()

and

getReferralContext()

(and appropriate
constructors and/or corresponding "set" methods).

The following code sample shows how

ReferralException

can be used.

```java
while (true) {
try {
bindings = ctx.listBindings(name);
while (bindings.hasMore()) {
b = bindings.next();
...
}
break;
} catch (ReferralException e) {
ctx = e.getReferralContext();
}
}
```

ReferralException

is an abstract class. Concrete implementations
determine its synchronization and serialization properties.

An environment parameter passed to the

getReferralContext()

method is owned by the caller.
The service provider will not modify the object or keep a reference to it,
but may keep a reference to a clone of it.

**Since:** 1.3
**See Also:** Serialized Form

public abstract class

ReferralException

extends

NamingException

This abstract class is used to represent a referral exception,
which is generated in response to a

referral

such as that returned by LDAP v3 servers.

A service provider provides
a subclass of

ReferralException

by providing implementations
for

getReferralInfo()

and

getReferralContext()

(and appropriate
constructors and/or corresponding "set" methods).

The following code sample shows how

ReferralException

can be used.

```java
while (true) {
try {
bindings = ctx.listBindings(name);
while (bindings.hasMore()) {
b = bindings.next();
...
}
break;
} catch (ReferralException e) {
ctx = e.getReferralContext();
}
}
```

ReferralException

is an abstract class. Concrete implementations
determine its synchronization and serialization properties.

An environment parameter passed to the

getReferralContext()

method is owned by the caller.
The service provider will not modify the object or keep a reference to it,
but may keep a reference to a clone of it.

A service provider provides
a subclass of

ReferralException

by providing implementations
for

getReferralInfo()

and

getReferralContext()

(and appropriate
constructors and/or corresponding "set" methods).

The following code sample shows how

ReferralException

can be used.

```java
while (true) {
try {
bindings = ctx.listBindings(name);
while (bindings.hasMore()) {
b = bindings.next();
...
}
break;
} catch (ReferralException e) {
ctx = e.getReferralContext();
}
}
```

ReferralException

is an abstract class. Concrete implementations
determine its synchronization and serialization properties.

An environment parameter passed to the

getReferralContext()

method is owned by the caller.
The service provider will not modify the object or keep a reference to it,
but may keep a reference to a clone of it.

The following code sample shows how

ReferralException

can be used.

```java
while (true) {
try {
bindings = ctx.listBindings(name);
while (bindings.hasMore()) {
b = bindings.next();
...
}
break;
} catch (ReferralException e) {
ctx = e.getReferralContext();
}
}
```

ReferralException

is an abstract class. Concrete implementations
determine its synchronization and serialization properties.

An environment parameter passed to the

getReferralContext()

method is owned by the caller.
The service provider will not modify the object or keep a reference to it,
but may keep a reference to a clone of it.

while (true) {
try {
bindings = ctx.listBindings(name);
while (bindings.hasMore()) {
b = bindings.next();
...
}
break;
} catch (ReferralException e) {
ctx = e.getReferralContext();
}
}

ReferralException

is an abstract class. Concrete implementations
determine its synchronization and serialization properties.

An environment parameter passed to the

getReferralContext()

method is owned by the caller.
The service provider will not modify the object or keep a reference to it,
but may keep a reference to a clone of it.

An environment parameter passed to the

getReferralContext()

method is owned by the caller.
The service provider will not modify the object or keep a reference to it,
but may keep a reference to a clone of it.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ReferralException

()

Constructs a new instance of ReferralException.

protected

ReferralException

​(

String

explanation)

Constructs a new instance of ReferralException using the
explanation supplied.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Context

getReferralContext

()

Retrieves the context at which to continue the method.

abstract

Context

getReferralContext

​(

Hashtable

<?,​?> env)

Retrieves the context at which to continue the method using
environment properties.

abstract

Object

getReferralInfo

()

Retrieves information (such as URLs) related to this referral.

abstract void

retryReferral

()

Retries the referral currently being processed.

abstract boolean

skipReferral

()

Discards the referral about to be processed.

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

wait

,

wait

,

wait

Field Summary

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Field Summary

Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Fields declared in class javax.naming. NamingException

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ReferralException

()

Constructs a new instance of ReferralException.

protected

ReferralException

​(

String

explanation)

Constructs a new instance of ReferralException using the
explanation supplied.

---

#### Constructor Summary

Constructs a new instance of ReferralException.

Constructs a new instance of ReferralException using the
explanation supplied.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Context

getReferralContext

()

Retrieves the context at which to continue the method.

abstract

Context

getReferralContext

​(

Hashtable

<?,​?> env)

Retrieves the context at which to continue the method using
environment properties.

abstract

Object

getReferralInfo

()

Retrieves information (such as URLs) related to this referral.

abstract void

retryReferral

()

Retries the referral currently being processed.

abstract boolean

skipReferral

()

Discards the referral about to be processed.

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

wait

,

wait

,

wait

---

#### Method Summary

Retrieves the context at which to continue the method.

Retrieves the context at which to continue the method using
environment properties.

Retrieves information (such as URLs) related to this referral.

Retries the referral currently being processed.

Discards the referral about to be processed.

Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

---

#### Methods declared in class javax.naming. NamingException

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ReferralException

```java
protected ReferralException​(
String
explanation)
```

Constructs a new instance of ReferralException using the
explanation supplied. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

- ReferralException

```java
protected ReferralException()
```

Constructs a new instance of ReferralException.
All fields are set to null.

============ METHOD DETAIL ==========

- Method Detail

- getReferralInfo

```java
public abstract
Object
getReferralInfo()
```

Retrieves information (such as URLs) related to this referral.
The program may examine or display this information
to the user to determine whether to continue with the referral,
or to determine additional information needs to be supplied in order
to continue with the referral.

**Returns:** Non-null referral information related to this referral.

- getReferralContext

```java
public abstract
Context
getReferralContext()
throws
NamingException
```

Retrieves the context at which to continue the method.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation. The referral context is
created using the environment properties of the context
that threw the ReferralException.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

**Returns:** The non-null context at which to continue the method.
**Throws:** NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

- getReferralContext

```java
public abstract
Context
getReferralContext​(
Hashtable
<?,​?> env)
throws
NamingException
```

Retrieves the context at which to continue the method using
environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.

The referral context is created using

env

as its environment
properties.
This method should be used instead of the no-arg overloaded form
when the caller needs to use different environment properties for
the referral context. It might need to do this, for example, when
it needs to supply different authentication information to the referred
server in order to create the referral context.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

**Parameters:** env

- The possibly null environment to use when retrieving the
referral context. If null, no environment properties will be used.
**Returns:** The non-null context at which to continue the method.
**Throws:** NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

- skipReferral

```java
public abstract boolean skipReferral()
```

Discards the referral about to be processed.
A call to this method should be followed by a call to

getReferralContext

to allow the processing of
other referrals to continue.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
if (!shallIFollow(e.getReferralInfo())) {
if (!e.skipReferral()) {
return;
}
}
ctx = e.getReferralContext();
}
```

**Returns:** true If more referral processing is pending; false otherwise.

- retryReferral

```java
public abstract void retryReferral()
```

Retries the referral currently being processed.
A call to this method should be followed by a call to

getReferralContext

to allow the current
referral to be retried.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
while (true) {
try {
ctx = e.getReferralContext(env);
break;
} catch (NamingException ne) {
if (! shallIRetry()) {
return;
}
// modify environment properties (env), if necessary
e.retryReferral();
}
}
}
```

Constructor Detail

- ReferralException

```java
protected ReferralException​(
String
explanation)
```

Constructs a new instance of ReferralException using the
explanation supplied. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

- ReferralException

```java
protected ReferralException()
```

Constructs a new instance of ReferralException.
All fields are set to null.

---

#### Constructor Detail

ReferralException

```java
protected ReferralException​(
String
explanation)
```

Constructs a new instance of ReferralException using the
explanation supplied. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

---

#### ReferralException

protected ReferralException​(

String

explanation)

Constructs a new instance of ReferralException using the
explanation supplied. All other fields are set to null.

ReferralException

```java
protected ReferralException()
```

Constructs a new instance of ReferralException.
All fields are set to null.

---

#### ReferralException

protected ReferralException()

Constructs a new instance of ReferralException.
All fields are set to null.

Method Detail

- getReferralInfo

```java
public abstract
Object
getReferralInfo()
```

Retrieves information (such as URLs) related to this referral.
The program may examine or display this information
to the user to determine whether to continue with the referral,
or to determine additional information needs to be supplied in order
to continue with the referral.

**Returns:** Non-null referral information related to this referral.

- getReferralContext

```java
public abstract
Context
getReferralContext()
throws
NamingException
```

Retrieves the context at which to continue the method.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation. The referral context is
created using the environment properties of the context
that threw the ReferralException.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

**Returns:** The non-null context at which to continue the method.
**Throws:** NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

- getReferralContext

```java
public abstract
Context
getReferralContext​(
Hashtable
<?,​?> env)
throws
NamingException
```

Retrieves the context at which to continue the method using
environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.

The referral context is created using

env

as its environment
properties.
This method should be used instead of the no-arg overloaded form
when the caller needs to use different environment properties for
the referral context. It might need to do this, for example, when
it needs to supply different authentication information to the referred
server in order to create the referral context.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

**Parameters:** env

- The possibly null environment to use when retrieving the
referral context. If null, no environment properties will be used.
**Returns:** The non-null context at which to continue the method.
**Throws:** NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

- skipReferral

```java
public abstract boolean skipReferral()
```

Discards the referral about to be processed.
A call to this method should be followed by a call to

getReferralContext

to allow the processing of
other referrals to continue.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
if (!shallIFollow(e.getReferralInfo())) {
if (!e.skipReferral()) {
return;
}
}
ctx = e.getReferralContext();
}
```

**Returns:** true If more referral processing is pending; false otherwise.

- retryReferral

```java
public abstract void retryReferral()
```

Retries the referral currently being processed.
A call to this method should be followed by a call to

getReferralContext

to allow the current
referral to be retried.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
while (true) {
try {
ctx = e.getReferralContext(env);
break;
} catch (NamingException ne) {
if (! shallIRetry()) {
return;
}
// modify environment properties (env), if necessary
e.retryReferral();
}
}
}
```

---

#### Method Detail

getReferralInfo

```java
public abstract
Object
getReferralInfo()
```

Retrieves information (such as URLs) related to this referral.
The program may examine or display this information
to the user to determine whether to continue with the referral,
or to determine additional information needs to be supplied in order
to continue with the referral.

**Returns:** Non-null referral information related to this referral.

---

#### getReferralInfo

public abstract

Object

getReferralInfo()

Retrieves information (such as URLs) related to this referral.
The program may examine or display this information
to the user to determine whether to continue with the referral,
or to determine additional information needs to be supplied in order
to continue with the referral.

getReferralContext

```java
public abstract
Context
getReferralContext()
throws
NamingException
```

Retrieves the context at which to continue the method.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation. The referral context is
created using the environment properties of the context
that threw the ReferralException.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

**Returns:** The non-null context at which to continue the method.
**Throws:** NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

---

#### getReferralContext

public abstract

Context

getReferralContext()
throws

NamingException

Retrieves the context at which to continue the method.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation. The referral context is
created using the environment properties of the context
that threw the ReferralException.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

getReferralContext

```java
public abstract
Context
getReferralContext​(
Hashtable
<?,​?> env)
throws
NamingException
```

Retrieves the context at which to continue the method using
environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.

The referral context is created using

env

as its environment
properties.
This method should be used instead of the no-arg overloaded form
when the caller needs to use different environment properties for
the referral context. It might need to do this, for example, when
it needs to supply different authentication information to the referred
server in order to create the referral context.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

**Parameters:** env

- The possibly null environment to use when retrieving the
referral context. If null, no environment properties will be used.
**Returns:** The non-null context at which to continue the method.
**Throws:** NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

---

#### getReferralContext

public abstract

Context

getReferralContext​(

Hashtable

<?,​?> env)
throws

NamingException

Retrieves the context at which to continue the method using
environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.

The referral context is created using

env

as its environment
properties.
This method should be used instead of the no-arg overloaded form
when the caller needs to use different environment properties for
the referral context. It might need to do this, for example, when
it needs to supply different authentication information to the referred
server in order to create the referral context.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

The referral context is created using

env

as its environment
properties.
This method should be used instead of the no-arg overloaded form
when the caller needs to use different environment properties for
the referral context. It might need to do this, for example, when
it needs to supply different authentication information to the referred
server in order to create the referral context.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

skipReferral

```java
public abstract boolean skipReferral()
```

Discards the referral about to be processed.
A call to this method should be followed by a call to

getReferralContext

to allow the processing of
other referrals to continue.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
if (!shallIFollow(e.getReferralInfo())) {
if (!e.skipReferral()) {
return;
}
}
ctx = e.getReferralContext();
}
```

**Returns:** true If more referral processing is pending; false otherwise.

---

#### skipReferral

public abstract boolean skipReferral()

Discards the referral about to be processed.
A call to this method should be followed by a call to

getReferralContext

to allow the processing of
other referrals to continue.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
if (!shallIFollow(e.getReferralInfo())) {
if (!e.skipReferral()) {
return;
}
}
ctx = e.getReferralContext();
}
```

} catch (ReferralException e) {
if (!shallIFollow(e.getReferralInfo())) {
if (!e.skipReferral()) {
return;
}
}
ctx = e.getReferralContext();
}

retryReferral

```java
public abstract void retryReferral()
```

Retries the referral currently being processed.
A call to this method should be followed by a call to

getReferralContext

to allow the current
referral to be retried.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
while (true) {
try {
ctx = e.getReferralContext(env);
break;
} catch (NamingException ne) {
if (! shallIRetry()) {
return;
}
// modify environment properties (env), if necessary
e.retryReferral();
}
}
}
```

---

#### retryReferral

public abstract void retryReferral()

Retries the referral currently being processed.
A call to this method should be followed by a call to

getReferralContext

to allow the current
referral to be retried.
The following code fragment shows a typical usage pattern.

```java
} catch (ReferralException e) {
while (true) {
try {
ctx = e.getReferralContext(env);
break;
} catch (NamingException ne) {
if (! shallIRetry()) {
return;
}
// modify environment properties (env), if necessary
e.retryReferral();
}
}
}
```

} catch (ReferralException e) {
while (true) {
try {
ctx = e.getReferralContext(env);
break;
} catch (NamingException ne) {
if (! shallIRetry()) {
return;
}
// modify environment properties (env), if necessary
e.retryReferral();
}
}
}

---

