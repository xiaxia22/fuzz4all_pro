# Class LdapReferralException

**Source:** `java.naming\javax\naming\ldap\LdapReferralException.html`

### Class Description

```java
public abstract class
LdapReferralException

extends
ReferralException
```

This abstract class is used to represent an LDAP referral exception.
It extends the base

ReferralException

by providing a

getReferralContext()

method that accepts request controls.
LdapReferralException is an abstract class. Concrete implementations of it
determine its synchronization and serialization properties.

A

Control[]

array passed as a parameter to
the

getReferralContext()

method is owned by the caller.
The service provider will not modify the array or keep a reference to it,
although it may keep references to the individual

Control

objects
in the array.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected LdapReferralException​(
String
explanation)

Constructs a new instance of LdapReferralException using the
explanation supplied. All other fields are set to null.

**Parameters:**
- explanation

- Additional detail about this exception. Can be null.

**See Also:**
- Throwable.getMessage()

---

#### protected LdapReferralException()

Constructs a new instance of LdapReferralException.
All fields are set to null.

---

### Method Details

#### public abstract
Context
getReferralContext()
throws
NamingException

Retrieves the context at which to continue the method using the
context's environment and no controls.
The referral context is created using the environment properties of
the context that threw the

ReferralException

and no controls.

This method is equivalent to

```java
getReferralContext(ctx.getEnvironment(), null);
```

where

ctx

is the context that threw the

ReferralException.

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

**Specified by:**
- getReferralContext

in class

ReferralException

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
environment properties and no controls.
The referral context is created using

env

as its environment
properties and no controls.

This method is equivalent to

```java
getReferralContext(env, null);
```

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

**Specified by:**
- getReferralContext

in class

ReferralException

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

#### public abstract
Context
getReferralContext​(
Hashtable
<?,​?> env,

Control
[] reqCtls)
throws
NamingException

Retrieves the context at which to continue the method using
request controls and environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.
To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

reqCtls

is used when creating the connection to the referred
server. These controls will be used as the connection request controls for
the context and context instances
derived from the context.

reqCtls

will also be the context's request controls for
subsequent context operations. See the

LdapContext

class
description for details.

This method should be used instead of the other two overloaded forms
when the caller needs to supply request controls for creating
the referral context. It might need to do this, for example, when
it needs to supply special controls relating to authentication.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

**Parameters:**
- reqCtls

- The possibly null request controls to use for the new context.
If null or the empty array means use no request controls.
- env

- The possibly null environment properties to use when
for the new context. If null, the context is initialized with no environment
properties.

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

### Additional Sections

#### Class LdapReferralException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ReferralException
- - javax.naming.ldap.LdapReferralException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ReferralException
- - javax.naming.ldap.LdapReferralException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.ReferralException
- - javax.naming.ldap.LdapReferralException

javax.naming.NamingException

- javax.naming.ReferralException
- - javax.naming.ldap.LdapReferralException

javax.naming.ReferralException

- javax.naming.ldap.LdapReferralException

javax.naming.ldap.LdapReferralException

**All Implemented Interfaces:** Serializable

```java
public abstract class
LdapReferralException

extends
ReferralException
```

This abstract class is used to represent an LDAP referral exception.
It extends the base

ReferralException

by providing a

getReferralContext()

method that accepts request controls.
LdapReferralException is an abstract class. Concrete implementations of it
determine its synchronization and serialization properties.

A

Control[]

array passed as a parameter to
the

getReferralContext()

method is owned by the caller.
The service provider will not modify the array or keep a reference to it,
although it may keep references to the individual

Control

objects
in the array.

**Since:** 1.3
**See Also:** Serialized Form

public abstract class

LdapReferralException

extends

ReferralException

This abstract class is used to represent an LDAP referral exception.
It extends the base

ReferralException

by providing a

getReferralContext()

method that accepts request controls.
LdapReferralException is an abstract class. Concrete implementations of it
determine its synchronization and serialization properties.

A

Control[]

array passed as a parameter to
the

getReferralContext()

method is owned by the caller.
The service provider will not modify the array or keep a reference to it,
although it may keep references to the individual

Control

objects
in the array.

A

Control[]

array passed as a parameter to
the

getReferralContext()

method is owned by the caller.
The service provider will not modify the array or keep a reference to it,
although it may keep references to the individual

Control

objects
in the array.

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

LdapReferralException

()

Constructs a new instance of LdapReferralException.

protected

LdapReferralException

​(

String

explanation)

Constructs a new instance of LdapReferralException using the
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

Retrieves the context at which to continue the method using the
context's environment and no controls.

abstract

Context

getReferralContext

​(

Hashtable

<?,​?> env)

Retrieves the context at which to continue the method using
environment properties and no controls.

abstract

Context

getReferralContext

​(

Hashtable

<?,​?> env,

Control

[] reqCtls)

Retrieves the context at which to continue the method using
request controls and environment properties.

- Methods declared in class javax.naming.

ReferralException

getReferralInfo

,

retryReferral

,

skipReferral

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

LdapReferralException

()

Constructs a new instance of LdapReferralException.

protected

LdapReferralException

​(

String

explanation)

Constructs a new instance of LdapReferralException using the
explanation supplied.

---

#### Constructor Summary

Constructs a new instance of LdapReferralException.

Constructs a new instance of LdapReferralException using the
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

Retrieves the context at which to continue the method using the
context's environment and no controls.

abstract

Context

getReferralContext

​(

Hashtable

<?,​?> env)

Retrieves the context at which to continue the method using
environment properties and no controls.

abstract

Context

getReferralContext

​(

Hashtable

<?,​?> env,

Control

[] reqCtls)

Retrieves the context at which to continue the method using
request controls and environment properties.

- Methods declared in class javax.naming.

ReferralException

getReferralInfo

,

retryReferral

,

skipReferral

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

Retrieves the context at which to continue the method using the
context's environment and no controls.

Retrieves the context at which to continue the method using
environment properties and no controls.

Retrieves the context at which to continue the method using
request controls and environment properties.

Methods declared in class javax.naming.

ReferralException

getReferralInfo

,

retryReferral

,

skipReferral

---

#### Methods declared in class javax.naming. ReferralException

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

- LdapReferralException

```java
protected LdapReferralException​(
String
explanation)
```

Constructs a new instance of LdapReferralException using the
explanation supplied. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

- LdapReferralException

```java
protected LdapReferralException()
```

Constructs a new instance of LdapReferralException.
All fields are set to null.

============ METHOD DETAIL ==========

- Method Detail

- getReferralContext

```java
public abstract
Context
getReferralContext()
throws
NamingException
```

Retrieves the context at which to continue the method using the
context's environment and no controls.
The referral context is created using the environment properties of
the context that threw the

ReferralException

and no controls.

This method is equivalent to

```java
getReferralContext(ctx.getEnvironment(), null);
```

where

ctx

is the context that threw the

ReferralException.

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

**Specified by:** getReferralContext

in class

ReferralException
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
environment properties and no controls.
The referral context is created using

env

as its environment
properties and no controls.

This method is equivalent to

```java
getReferralContext(env, null);
```

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

**Specified by:** getReferralContext

in class

ReferralException
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

- getReferralContext

```java
public abstract
Context
getReferralContext​(
Hashtable
<?,​?> env,

Control
[] reqCtls)
throws
NamingException
```

Retrieves the context at which to continue the method using
request controls and environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.
To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

reqCtls

is used when creating the connection to the referred
server. These controls will be used as the connection request controls for
the context and context instances
derived from the context.

reqCtls

will also be the context's request controls for
subsequent context operations. See the

LdapContext

class
description for details.

This method should be used instead of the other two overloaded forms
when the caller needs to supply request controls for creating
the referral context. It might need to do this, for example, when
it needs to supply special controls relating to authentication.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

**Parameters:** reqCtls

- The possibly null request controls to use for the new context.
If null or the empty array means use no request controls.
**Parameters:** env

- The possibly null environment properties to use when
for the new context. If null, the context is initialized with no environment
properties.
**Returns:** The non-null context at which to continue the method.
**Throws:** NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

Constructor Detail

- LdapReferralException

```java
protected LdapReferralException​(
String
explanation)
```

Constructs a new instance of LdapReferralException using the
explanation supplied. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

- LdapReferralException

```java
protected LdapReferralException()
```

Constructs a new instance of LdapReferralException.
All fields are set to null.

---

#### Constructor Detail

LdapReferralException

```java
protected LdapReferralException​(
String
explanation)
```

Constructs a new instance of LdapReferralException using the
explanation supplied. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

---

#### LdapReferralException

protected LdapReferralException​(

String

explanation)

Constructs a new instance of LdapReferralException using the
explanation supplied. All other fields are set to null.

LdapReferralException

```java
protected LdapReferralException()
```

Constructs a new instance of LdapReferralException.
All fields are set to null.

---

#### LdapReferralException

protected LdapReferralException()

Constructs a new instance of LdapReferralException.
All fields are set to null.

Method Detail

- getReferralContext

```java
public abstract
Context
getReferralContext()
throws
NamingException
```

Retrieves the context at which to continue the method using the
context's environment and no controls.
The referral context is created using the environment properties of
the context that threw the

ReferralException

and no controls.

This method is equivalent to

```java
getReferralContext(ctx.getEnvironment(), null);
```

where

ctx

is the context that threw the

ReferralException.

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

**Specified by:** getReferralContext

in class

ReferralException
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
environment properties and no controls.
The referral context is created using

env

as its environment
properties and no controls.

This method is equivalent to

```java
getReferralContext(env, null);
```

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

**Specified by:** getReferralContext

in class

ReferralException
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

- getReferralContext

```java
public abstract
Context
getReferralContext​(
Hashtable
<?,​?> env,

Control
[] reqCtls)
throws
NamingException
```

Retrieves the context at which to continue the method using
request controls and environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.
To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

reqCtls

is used when creating the connection to the referred
server. These controls will be used as the connection request controls for
the context and context instances
derived from the context.

reqCtls

will also be the context's request controls for
subsequent context operations. See the

LdapContext

class
description for details.

This method should be used instead of the other two overloaded forms
when the caller needs to supply request controls for creating
the referral context. It might need to do this, for example, when
it needs to supply special controls relating to authentication.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

**Parameters:** reqCtls

- The possibly null request controls to use for the new context.
If null or the empty array means use no request controls.
**Parameters:** env

- The possibly null environment properties to use when
for the new context. If null, the context is initialized with no environment
properties.
**Returns:** The non-null context at which to continue the method.
**Throws:** NamingException

- If a naming exception was encountered.
Call either

retryReferral()

or

skipReferral()

to continue processing referrals.

---

#### Method Detail

getReferralContext

```java
public abstract
Context
getReferralContext()
throws
NamingException
```

Retrieves the context at which to continue the method using the
context's environment and no controls.
The referral context is created using the environment properties of
the context that threw the

ReferralException

and no controls.

This method is equivalent to

```java
getReferralContext(ctx.getEnvironment(), null);
```

where

ctx

is the context that threw the

ReferralException.

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

**Specified by:** getReferralContext

in class

ReferralException
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

Retrieves the context at which to continue the method using the
context's environment and no controls.
The referral context is created using the environment properties of
the context that threw the

ReferralException

and no controls.

This method is equivalent to

```java
getReferralContext(ctx.getEnvironment(), null);
```

where

ctx

is the context that threw the

ReferralException.

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

This method is equivalent to

```java
getReferralContext(ctx.getEnvironment(), null);
```

where

ctx

is the context that threw the

ReferralException.

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

getReferralContext(ctx.getEnvironment(), null);

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

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
environment properties and no controls.
The referral context is created using

env

as its environment
properties and no controls.

This method is equivalent to

```java
getReferralContext(env, null);
```

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

**Specified by:** getReferralContext

in class

ReferralException
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
environment properties and no controls.
The referral context is created using

env

as its environment
properties and no controls.

This method is equivalent to

```java
getReferralContext(env, null);
```

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

This method is equivalent to

```java
getReferralContext(env, null);
```

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

getReferralContext(env, null);

It is overridden in this class for documentation purposes only.
See

ReferralException

for how to use this method.

getReferralContext

```java
public abstract
Context
getReferralContext​(
Hashtable
<?,​?> env,

Control
[] reqCtls)
throws
NamingException
```

Retrieves the context at which to continue the method using
request controls and environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.
To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

reqCtls

is used when creating the connection to the referred
server. These controls will be used as the connection request controls for
the context and context instances
derived from the context.

reqCtls

will also be the context's request controls for
subsequent context operations. See the

LdapContext

class
description for details.

This method should be used instead of the other two overloaded forms
when the caller needs to supply request controls for creating
the referral context. It might need to do this, for example, when
it needs to supply special controls relating to authentication.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

**Parameters:** reqCtls

- The possibly null request controls to use for the new context.
If null or the empty array means use no request controls.
**Parameters:** env

- The possibly null environment properties to use when
for the new context. If null, the context is initialized with no environment
properties.
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

<?,​?> env,

Control

[] reqCtls)
throws

NamingException

Retrieves the context at which to continue the method using
request controls and environment properties.
Regardless of whether a referral is encountered directly during a
context operation, or indirectly, for example, during a search
enumeration, the referral exception should provide a context
at which to continue the operation.
To continue the operation, the client program should re-invoke
the method using the same arguments as the original invocation.

reqCtls

is used when creating the connection to the referred
server. These controls will be used as the connection request controls for
the context and context instances
derived from the context.

reqCtls

will also be the context's request controls for
subsequent context operations. See the

LdapContext

class
description for details.

This method should be used instead of the other two overloaded forms
when the caller needs to supply request controls for creating
the referral context. It might need to do this, for example, when
it needs to supply special controls relating to authentication.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

reqCtls

is used when creating the connection to the referred
server. These controls will be used as the connection request controls for
the context and context instances
derived from the context.

reqCtls

will also be the context's request controls for
subsequent context operations. See the

LdapContext

class
description for details.

This method should be used instead of the other two overloaded forms
when the caller needs to supply request controls for creating
the referral context. It might need to do this, for example, when
it needs to supply special controls relating to authentication.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

This method should be used instead of the other two overloaded forms
when the caller needs to supply request controls for creating
the referral context. It might need to do this, for example, when
it needs to supply special controls relating to authentication.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

Service provider implementors should read the "Service Provider" section
in the

LdapContext

class description for implementation details.

---

