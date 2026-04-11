# Class RemoteObjectInvocationHandler

**Source:** `java.rmi\java\rmi\server\RemoteObjectInvocationHandler.html`

### Class Description

```java
public class
RemoteObjectInvocationHandler

extends
RemoteObject

implements
InvocationHandler
```

An implementation of the

InvocationHandler

interface for
use with Java Remote Method Invocation (Java RMI). This invocation
handler can be used in conjunction with a dynamic proxy instance as a
replacement for a pregenerated stub class.

Applications are not expected to use this class directly. A remote
object exported to use a dynamic proxy with

UnicastRemoteObject

or

Activatable

has an instance of this class as that proxy's
invocation handler.

**All Implemented Interfaces:** Serializable

,

InvocationHandler

,

Remote

---

### Field Details

*No entries found.*

### Constructor Details

#### public RemoteObjectInvocationHandler​(
RemoteRef
ref)

Creates a new

RemoteObjectInvocationHandler

constructed
with the specified

RemoteRef

.

**Parameters:**
- ref

- the remote ref

**Throws:**
- NullPointerException

- if

ref

is

null

---

### Method Details

#### public
Object
invoke​(
Object
proxy,

Method
method,

Object
[] args)
throws
Throwable

Processes a method invocation made on the encapsulating
proxy instance,

proxy

, and returns the result.

RemoteObjectInvocationHandler

implements this method
as follows:

If

method

is one of the following methods, it
is processed as described below:

- Object.hashCode

: Returns the hash
code value for the proxy.

Object.equals

: Returns

true

if the argument (

args[0]

) is an instance of a dynamic
proxy class and this invocation handler is equal to the invocation
handler of that argument, and returns

false

otherwise.

Object.toString

: Returns a string
representation of the proxy.

If

method

overrides

Object.finalize

,
it is ignored.

Otherwise, a remote call is made as follows:

- If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

**Specified by:**
- invoke

in interface

InvocationHandler

**Parameters:**
- proxy

- the proxy instance that the method was invoked on
- method

- the

Method

instance corresponding to the
interface method invoked on the proxy instance
- args

- an array of objects containing the values of the
arguments passed in the method invocation on the proxy instance, or

null

if the method takes no arguments

**Returns:**
- the value to return from the method invocation on the proxy
instance

**Throws:**
- Throwable

- the exception to throw from the method invocation
on the proxy instance

**See Also:**
- UndeclaredThrowableException

---

### Additional Sections

#### Class RemoteObjectInvocationHandler

java.lang.Object

- java.rmi.server.RemoteObject
- - java.rmi.server.RemoteObjectInvocationHandler

java.rmi.server.RemoteObject

- java.rmi.server.RemoteObjectInvocationHandler

java.rmi.server.RemoteObjectInvocationHandler

**All Implemented Interfaces:** Serializable

,

InvocationHandler

,

Remote

```java
public class
RemoteObjectInvocationHandler

extends
RemoteObject

implements
InvocationHandler
```

An implementation of the

InvocationHandler

interface for
use with Java Remote Method Invocation (Java RMI). This invocation
handler can be used in conjunction with a dynamic proxy instance as a
replacement for a pregenerated stub class.

Applications are not expected to use this class directly. A remote
object exported to use a dynamic proxy with

UnicastRemoteObject

or

Activatable

has an instance of this class as that proxy's
invocation handler.

**Since:** 1.5
**See Also:** Serialized Form

public class

RemoteObjectInvocationHandler

extends

RemoteObject

implements

InvocationHandler

An implementation of the

InvocationHandler

interface for
use with Java Remote Method Invocation (Java RMI). This invocation
handler can be used in conjunction with a dynamic proxy instance as a
replacement for a pregenerated stub class.

Applications are not expected to use this class directly. A remote
object exported to use a dynamic proxy with

UnicastRemoteObject

or

Activatable

has an instance of this class as that proxy's
invocation handler.

Applications are not expected to use this class directly. A remote
object exported to use a dynamic proxy with

UnicastRemoteObject

or

Activatable

has an instance of this class as that proxy's
invocation handler.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.rmi.server.

RemoteObject

ref

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RemoteObjectInvocationHandler

​(

RemoteRef

ref)

Creates a new

RemoteObjectInvocationHandler

constructed
with the specified

RemoteRef

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

invoke

​(

Object

proxy,

Method

method,

Object

[] args)

Processes a method invocation made on the encapsulating
proxy instance,

proxy

, and returns the result.

- Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

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

Field Summary

- Fields declared in class java.rmi.server.

RemoteObject

ref

---

#### Field Summary

Fields declared in class java.rmi.server.

RemoteObject

ref

---

#### Fields declared in class java.rmi.server. RemoteObject

Constructor Summary

Constructors

Constructor

Description

RemoteObjectInvocationHandler

​(

RemoteRef

ref)

Creates a new

RemoteObjectInvocationHandler

constructed
with the specified

RemoteRef

.

---

#### Constructor Summary

Creates a new

RemoteObjectInvocationHandler

constructed
with the specified

RemoteRef

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

invoke

​(

Object

proxy,

Method

method,

Object

[] args)

Processes a method invocation made on the encapsulating
proxy instance,

proxy

, and returns the result.

- Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

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

Processes a method invocation made on the encapsulating
proxy instance,

proxy

, and returns the result.

Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

---

#### Methods declared in class java.rmi.server. RemoteObject

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

- RemoteObjectInvocationHandler

```java
public RemoteObjectInvocationHandler​(
RemoteRef
ref)
```

Creates a new

RemoteObjectInvocationHandler

constructed
with the specified

RemoteRef

.

**Parameters:** ref

- the remote ref
**Throws:** NullPointerException

- if

ref

is

null

============ METHOD DETAIL ==========

- Method Detail

- invoke

```java
public
Object
invoke​(
Object
proxy,

Method
method,

Object
[] args)
throws
Throwable
```

Processes a method invocation made on the encapsulating
proxy instance,

proxy

, and returns the result.

RemoteObjectInvocationHandler

implements this method
as follows:

If

method

is one of the following methods, it
is processed as described below:

- Object.hashCode

: Returns the hash
code value for the proxy.

Object.equals

: Returns

true

if the argument (

args[0]

) is an instance of a dynamic
proxy class and this invocation handler is equal to the invocation
handler of that argument, and returns

false

otherwise.

Object.toString

: Returns a string
representation of the proxy.

If

method

overrides

Object.finalize

,
it is ignored.

Otherwise, a remote call is made as follows:

- If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

**Specified by:** invoke

in interface

InvocationHandler
**Parameters:** proxy

- the proxy instance that the method was invoked on
**Parameters:** method

- the

Method

instance corresponding to the
interface method invoked on the proxy instance
**Parameters:** args

- an array of objects containing the values of the
arguments passed in the method invocation on the proxy instance, or

null

if the method takes no arguments
**Returns:** the value to return from the method invocation on the proxy
instance
**Throws:** Throwable

- the exception to throw from the method invocation
on the proxy instance
**See Also:** UndeclaredThrowableException

Constructor Detail

- RemoteObjectInvocationHandler

```java
public RemoteObjectInvocationHandler​(
RemoteRef
ref)
```

Creates a new

RemoteObjectInvocationHandler

constructed
with the specified

RemoteRef

.

**Parameters:** ref

- the remote ref
**Throws:** NullPointerException

- if

ref

is

null

---

#### Constructor Detail

RemoteObjectInvocationHandler

```java
public RemoteObjectInvocationHandler​(
RemoteRef
ref)
```

Creates a new

RemoteObjectInvocationHandler

constructed
with the specified

RemoteRef

.

**Parameters:** ref

- the remote ref
**Throws:** NullPointerException

- if

ref

is

null

---

#### RemoteObjectInvocationHandler

public RemoteObjectInvocationHandler​(

RemoteRef

ref)

Creates a new

RemoteObjectInvocationHandler

constructed
with the specified

RemoteRef

.

Method Detail

- invoke

```java
public
Object
invoke​(
Object
proxy,

Method
method,

Object
[] args)
throws
Throwable
```

Processes a method invocation made on the encapsulating
proxy instance,

proxy

, and returns the result.

RemoteObjectInvocationHandler

implements this method
as follows:

If

method

is one of the following methods, it
is processed as described below:

- Object.hashCode

: Returns the hash
code value for the proxy.

Object.equals

: Returns

true

if the argument (

args[0]

) is an instance of a dynamic
proxy class and this invocation handler is equal to the invocation
handler of that argument, and returns

false

otherwise.

Object.toString

: Returns a string
representation of the proxy.

If

method

overrides

Object.finalize

,
it is ignored.

Otherwise, a remote call is made as follows:

- If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

**Specified by:** invoke

in interface

InvocationHandler
**Parameters:** proxy

- the proxy instance that the method was invoked on
**Parameters:** method

- the

Method

instance corresponding to the
interface method invoked on the proxy instance
**Parameters:** args

- an array of objects containing the values of the
arguments passed in the method invocation on the proxy instance, or

null

if the method takes no arguments
**Returns:** the value to return from the method invocation on the proxy
instance
**Throws:** Throwable

- the exception to throw from the method invocation
on the proxy instance
**See Also:** UndeclaredThrowableException

---

#### Method Detail

invoke

```java
public
Object
invoke​(
Object
proxy,

Method
method,

Object
[] args)
throws
Throwable
```

Processes a method invocation made on the encapsulating
proxy instance,

proxy

, and returns the result.

RemoteObjectInvocationHandler

implements this method
as follows:

If

method

is one of the following methods, it
is processed as described below:

- Object.hashCode

: Returns the hash
code value for the proxy.

Object.equals

: Returns

true

if the argument (

args[0]

) is an instance of a dynamic
proxy class and this invocation handler is equal to the invocation
handler of that argument, and returns

false

otherwise.

Object.toString

: Returns a string
representation of the proxy.

If

method

overrides

Object.finalize

,
it is ignored.

Otherwise, a remote call is made as follows:

- If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

**Specified by:** invoke

in interface

InvocationHandler
**Parameters:** proxy

- the proxy instance that the method was invoked on
**Parameters:** method

- the

Method

instance corresponding to the
interface method invoked on the proxy instance
**Parameters:** args

- an array of objects containing the values of the
arguments passed in the method invocation on the proxy instance, or

null

if the method takes no arguments
**Returns:** the value to return from the method invocation on the proxy
instance
**Throws:** Throwable

- the exception to throw from the method invocation
on the proxy instance
**See Also:** UndeclaredThrowableException

---

#### invoke

public

Object

invoke​(

Object

proxy,

Method

method,

Object

[] args)
throws

Throwable

Processes a method invocation made on the encapsulating
proxy instance,

proxy

, and returns the result.

RemoteObjectInvocationHandler

implements this method
as follows:

If

method

is one of the following methods, it
is processed as described below:

- Object.hashCode

: Returns the hash
code value for the proxy.

Object.equals

: Returns

true

if the argument (

args[0]

) is an instance of a dynamic
proxy class and this invocation handler is equal to the invocation
handler of that argument, and returns

false

otherwise.

Object.toString

: Returns a string
representation of the proxy.

If

method

overrides

Object.finalize

,
it is ignored.

Otherwise, a remote call is made as follows:

- If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

RemoteObjectInvocationHandler

implements this method
as follows:

If

method

is one of the following methods, it
is processed as described below:

- Object.hashCode

: Returns the hash
code value for the proxy.

Object.equals

: Returns

true

if the argument (

args[0]

) is an instance of a dynamic
proxy class and this invocation handler is equal to the invocation
handler of that argument, and returns

false

otherwise.

Object.toString

: Returns a string
representation of the proxy.

If

method

overrides

Object.finalize

,
it is ignored.

Otherwise, a remote call is made as follows:

- If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

If

method

is one of the following methods, it
is processed as described below:

- Object.hashCode

: Returns the hash
code value for the proxy.

Object.equals

: Returns

true

if the argument (

args[0]

) is an instance of a dynamic
proxy class and this invocation handler is equal to the invocation
handler of that argument, and returns

false

otherwise.

Object.toString

: Returns a string
representation of the proxy.

If

method

overrides

Object.finalize

,
it is ignored.

Otherwise, a remote call is made as follows:

- If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

Object.hashCode

: Returns the hash
code value for the proxy.

Object.equals

: Returns

true

if the argument (

args[0]

) is an instance of a dynamic
proxy class and this invocation handler is equal to the invocation
handler of that argument, and returns

false

otherwise.

Object.toString

: Returns a string
representation of the proxy.

If

method

overrides

Object.finalize

,
it is ignored.

Otherwise, a remote call is made as follows:

- If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

Otherwise, a remote call is made as follows:

- If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

If

proxy

is not an instance of the interface

Remote

, then an

IllegalArgumentException

is thrown.

Otherwise, the

invoke

method is invoked
on this invocation handler's

RemoteRef

, passing

proxy

,

method

,

args

, and the
method hash (defined in section 8.3 of the "Java Remote Method
Invocation (RMI) Specification") for

method

, and the
result is returned.

If an exception is thrown by

RemoteRef.invoke

and
that exception is a checked exception that is not assignable to any
exception in the

throws

clause of the method
implemented by the

proxy

's class, then that exception
is wrapped in an

UnexpectedException

and the wrapped
exception is thrown. Otherwise, the exception thrown by

invoke

is thrown by this method.

The semantics of this method are unspecified if the
arguments could not have been produced by an instance of some
valid dynamic proxy class containing this invocation handler.

---

