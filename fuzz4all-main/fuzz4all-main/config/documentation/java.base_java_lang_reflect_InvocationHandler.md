# Interface InvocationHandler

**Source:** `java.base\java\lang\reflect\InvocationHandler.html`

### Class Description

```java
public interface
InvocationHandler
```

InvocationHandler

is the interface implemented by
the

invocation handler

of a proxy instance.

Each proxy instance has an associated invocation handler.
When a method is invoked on a proxy instance, the method
invocation is encoded and dispatched to the

invoke

method of its invocation handler.

**All Known Implementing Classes:** CompositeDataInvocationHandler

,

EventHandler

,

MBeanServerInvocationHandler

,

RemoteObjectInvocationHandler

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
invoke​(
Object
proxy,

Method
method,

Object
[] args)
throws
Throwable

Processes a method invocation on a proxy instance and returns
the result. This method will be invoked on an invocation handler
when a method is invoked on a proxy instance that it is
associated with.

**Parameters:**
- proxy

- the proxy instance that the method was invoked on
- method

- the

Method

instance corresponding to
the interface method invoked on the proxy instance. The declaring
class of the

Method

object will be the interface that
the method was declared in, which may be a superinterface of the
proxy interface that the proxy class inherits the method through.
- args

- an array of objects containing the values of the
arguments passed in the method invocation on the proxy instance,
or

null

if interface method takes no arguments.
Arguments of primitive types are wrapped in instances of the
appropriate primitive wrapper class, such as

java.lang.Integer

or

java.lang.Boolean

.

**Returns:**
- the value to return from the method invocation on the
proxy instance. If the declared return type of the interface
method is a primitive type, then the value returned by
this method must be an instance of the corresponding primitive
wrapper class; otherwise, it must be a type assignable to the
declared return type. If the value returned by this method is

null

and the interface method's return type is
primitive, then a

NullPointerException

will be
thrown by the method invocation on the proxy instance. If the
value returned by this method is otherwise not compatible with
the interface method's declared return type as described above,
a

ClassCastException

will be thrown by the method
invocation on the proxy instance.

**Throws:**
- Throwable

- the exception to throw from the method
invocation on the proxy instance. The exception's type must be
assignable either to any of the exception types declared in the

throws

clause of the interface method or to the
unchecked exception types

java.lang.RuntimeException

or

java.lang.Error

. If a checked exception is
thrown by this method that is not assignable to any of the
exception types declared in the

throws

clause of
the interface method, then an

UndeclaredThrowableException

containing the
exception that was thrown by this method will be thrown by the
method invocation on the proxy instance.

**See Also:**
- UndeclaredThrowableException

---

### Additional Sections

#### Interface InvocationHandler

**All Known Implementing Classes:** CompositeDataInvocationHandler

,

EventHandler

,

MBeanServerInvocationHandler

,

RemoteObjectInvocationHandler

```java
public interface
InvocationHandler
```

InvocationHandler

is the interface implemented by
the

invocation handler

of a proxy instance.

Each proxy instance has an associated invocation handler.
When a method is invoked on a proxy instance, the method
invocation is encoded and dispatched to the

invoke

method of its invocation handler.

**Since:** 1.3
**See Also:** Proxy

public interface

InvocationHandler

InvocationHandler

is the interface implemented by
the

invocation handler

of a proxy instance.

Each proxy instance has an associated invocation handler.
When a method is invoked on a proxy instance, the method
invocation is encoded and dispatched to the

invoke

method of its invocation handler.

Each proxy instance has an associated invocation handler.
When a method is invoked on a proxy instance, the method
invocation is encoded and dispatched to the

invoke

method of its invocation handler.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

Processes a method invocation on a proxy instance and returns
the result.

Method Summary

All Methods

Instance Methods

Abstract Methods

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

Processes a method invocation on a proxy instance and returns
the result.

---

#### Method Summary

Processes a method invocation on a proxy instance and returns
the result.

============ METHOD DETAIL ==========

- Method Detail

- invoke

```java
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

Processes a method invocation on a proxy instance and returns
the result. This method will be invoked on an invocation handler
when a method is invoked on a proxy instance that it is
associated with.

**Parameters:** proxy

- the proxy instance that the method was invoked on
**Parameters:** method

- the

Method

instance corresponding to
the interface method invoked on the proxy instance. The declaring
class of the

Method

object will be the interface that
the method was declared in, which may be a superinterface of the
proxy interface that the proxy class inherits the method through.
**Parameters:** args

- an array of objects containing the values of the
arguments passed in the method invocation on the proxy instance,
or

null

if interface method takes no arguments.
Arguments of primitive types are wrapped in instances of the
appropriate primitive wrapper class, such as

java.lang.Integer

or

java.lang.Boolean

.
**Returns:** the value to return from the method invocation on the
proxy instance. If the declared return type of the interface
method is a primitive type, then the value returned by
this method must be an instance of the corresponding primitive
wrapper class; otherwise, it must be a type assignable to the
declared return type. If the value returned by this method is

null

and the interface method's return type is
primitive, then a

NullPointerException

will be
thrown by the method invocation on the proxy instance. If the
value returned by this method is otherwise not compatible with
the interface method's declared return type as described above,
a

ClassCastException

will be thrown by the method
invocation on the proxy instance.
**Throws:** Throwable

- the exception to throw from the method
invocation on the proxy instance. The exception's type must be
assignable either to any of the exception types declared in the

throws

clause of the interface method or to the
unchecked exception types

java.lang.RuntimeException

or

java.lang.Error

. If a checked exception is
thrown by this method that is not assignable to any of the
exception types declared in the

throws

clause of
the interface method, then an

UndeclaredThrowableException

containing the
exception that was thrown by this method will be thrown by the
method invocation on the proxy instance.
**See Also:** UndeclaredThrowableException

Method Detail

- invoke

```java
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

Processes a method invocation on a proxy instance and returns
the result. This method will be invoked on an invocation handler
when a method is invoked on a proxy instance that it is
associated with.

**Parameters:** proxy

- the proxy instance that the method was invoked on
**Parameters:** method

- the

Method

instance corresponding to
the interface method invoked on the proxy instance. The declaring
class of the

Method

object will be the interface that
the method was declared in, which may be a superinterface of the
proxy interface that the proxy class inherits the method through.
**Parameters:** args

- an array of objects containing the values of the
arguments passed in the method invocation on the proxy instance,
or

null

if interface method takes no arguments.
Arguments of primitive types are wrapped in instances of the
appropriate primitive wrapper class, such as

java.lang.Integer

or

java.lang.Boolean

.
**Returns:** the value to return from the method invocation on the
proxy instance. If the declared return type of the interface
method is a primitive type, then the value returned by
this method must be an instance of the corresponding primitive
wrapper class; otherwise, it must be a type assignable to the
declared return type. If the value returned by this method is

null

and the interface method's return type is
primitive, then a

NullPointerException

will be
thrown by the method invocation on the proxy instance. If the
value returned by this method is otherwise not compatible with
the interface method's declared return type as described above,
a

ClassCastException

will be thrown by the method
invocation on the proxy instance.
**Throws:** Throwable

- the exception to throw from the method
invocation on the proxy instance. The exception's type must be
assignable either to any of the exception types declared in the

throws

clause of the interface method or to the
unchecked exception types

java.lang.RuntimeException

or

java.lang.Error

. If a checked exception is
thrown by this method that is not assignable to any of the
exception types declared in the

throws

clause of
the interface method, then an

UndeclaredThrowableException

containing the
exception that was thrown by this method will be thrown by the
method invocation on the proxy instance.
**See Also:** UndeclaredThrowableException

---

#### Method Detail

invoke

```java
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

Processes a method invocation on a proxy instance and returns
the result. This method will be invoked on an invocation handler
when a method is invoked on a proxy instance that it is
associated with.

**Parameters:** proxy

- the proxy instance that the method was invoked on
**Parameters:** method

- the

Method

instance corresponding to
the interface method invoked on the proxy instance. The declaring
class of the

Method

object will be the interface that
the method was declared in, which may be a superinterface of the
proxy interface that the proxy class inherits the method through.
**Parameters:** args

- an array of objects containing the values of the
arguments passed in the method invocation on the proxy instance,
or

null

if interface method takes no arguments.
Arguments of primitive types are wrapped in instances of the
appropriate primitive wrapper class, such as

java.lang.Integer

or

java.lang.Boolean

.
**Returns:** the value to return from the method invocation on the
proxy instance. If the declared return type of the interface
method is a primitive type, then the value returned by
this method must be an instance of the corresponding primitive
wrapper class; otherwise, it must be a type assignable to the
declared return type. If the value returned by this method is

null

and the interface method's return type is
primitive, then a

NullPointerException

will be
thrown by the method invocation on the proxy instance. If the
value returned by this method is otherwise not compatible with
the interface method's declared return type as described above,
a

ClassCastException

will be thrown by the method
invocation on the proxy instance.
**Throws:** Throwable

- the exception to throw from the method
invocation on the proxy instance. The exception's type must be
assignable either to any of the exception types declared in the

throws

clause of the interface method or to the
unchecked exception types

java.lang.RuntimeException

or

java.lang.Error

. If a checked exception is
thrown by this method that is not assignable to any of the
exception types declared in the

throws

clause of
the interface method, then an

UndeclaredThrowableException

containing the
exception that was thrown by this method will be thrown by the
method invocation on the proxy instance.
**See Also:** UndeclaredThrowableException

---

#### invoke

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

Processes a method invocation on a proxy instance and returns
the result. This method will be invoked on an invocation handler
when a method is invoked on a proxy instance that it is
associated with.

---

