# Interface Invocable

**Source:** `java.scripting\javax\script\Invocable.html`

### Class Description

```java
public interface
Invocable
```

The optional interface implemented by ScriptEngines whose methods allow the invocation of
procedures in scripts that have previously been executed.

**All Known Implementing Classes:** NashornScriptEngine

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
invokeMethod​(
Object
thiz,

String
name,

Object
... args)
throws
ScriptException
,

NoSuchMethodException

Calls a method on a script object compiled during a previous script execution,
which is retained in the state of the

ScriptEngine

.

**Parameters:**
- name

- The name of the procedure to be called.
- thiz

- If the procedure is a member of a class
defined in the script and thiz is an instance of that class
returned by a previous execution or invocation, the named method is
called through that instance.
- args

- Arguments to pass to the procedure. The rules for converting
the arguments to scripting variables are implementation-specific.

**Returns:**
- The value returned by the procedure. The rules for converting the scripting
variable returned by the script method to a Java Object are implementation-specific.

**Throws:**
- ScriptException

- if an error occurs during invocation of the method.
- NoSuchMethodException

- if method with given name or matching argument types cannot be found.
- NullPointerException

- if the method name is null.
- IllegalArgumentException

- if the specified thiz is null or the specified Object is
does not represent a scripting object.

---

#### Object
invokeFunction​(
String
name,

Object
... args)
throws
ScriptException
,

NoSuchMethodException

Used to call top-level procedures and functions defined in scripts.

**Parameters:**
- name

- of the procedure or function to call
- args

- Arguments to pass to the procedure or function

**Returns:**
- The value returned by the procedure or function

**Throws:**
- ScriptException

- if an error occurs during invocation of the method.
- NoSuchMethodException

- if method with given name or matching argument types cannot be found.
- NullPointerException

- if method name is null.

---

#### <T> T getInterface​(
Class
<T> clasz)

Returns an implementation of an interface using functions compiled in
the interpreter. The methods of the interface
may be implemented using the

invokeFunction

method.

**Parameters:**
- clasz

- The

Class

object of the interface to return.

**Returns:**
- An instance of requested interface - null if the requested interface is unavailable,
i. e. if compiled functions in the

ScriptEngine

cannot be found matching
the ones in the requested interface.

**Throws:**
- IllegalArgumentException

- if the specified

Class

object
is null or is not an interface.

**Type Parameters:**
- T

- the type of the interface to return

---

#### <T> T getInterface​(
Object
thiz,

Class
<T> clasz)

Returns an implementation of an interface using member functions of
a scripting object compiled in the interpreter. The methods of the
interface may be implemented using the

invokeMethod

method.

**Parameters:**
- thiz

- The scripting object whose member functions are used to implement the methods of the interface.
- clasz

- The

Class

object of the interface to return.

**Returns:**
- An instance of requested interface - null if the requested interface is unavailable,
i. e. if compiled methods in the

ScriptEngine

cannot be found matching
the ones in the requested interface.

**Throws:**
- IllegalArgumentException

- if the specified

Class

object
is null or is not an interface, or if the specified Object is
null or does not represent a scripting object.

**Type Parameters:**
- T

- the type of the interface to return

---

### Additional Sections

#### Interface Invocable

**All Known Implementing Classes:** NashornScriptEngine

```java
public interface
Invocable
```

The optional interface implemented by ScriptEngines whose methods allow the invocation of
procedures in scripts that have previously been executed.

**Since:** 1.6

public interface

Invocable

The optional interface implemented by ScriptEngines whose methods allow the invocation of
procedures in scripts that have previously been executed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<T> T

getInterface

​(

Class

<T> clasz)

Returns an implementation of an interface using functions compiled in
the interpreter.

<T> T

getInterface

​(

Object

thiz,

Class

<T> clasz)

Returns an implementation of an interface using member functions of
a scripting object compiled in the interpreter.

Object

invokeFunction

​(

String

name,

Object

... args)

Used to call top-level procedures and functions defined in scripts.

Object

invokeMethod

​(

Object

thiz,

String

name,

Object

... args)

Calls a method on a script object compiled during a previous script execution,
which is retained in the state of the

ScriptEngine

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<T> T

getInterface

​(

Class

<T> clasz)

Returns an implementation of an interface using functions compiled in
the interpreter.

<T> T

getInterface

​(

Object

thiz,

Class

<T> clasz)

Returns an implementation of an interface using member functions of
a scripting object compiled in the interpreter.

Object

invokeFunction

​(

String

name,

Object

... args)

Used to call top-level procedures and functions defined in scripts.

Object

invokeMethod

​(

Object

thiz,

String

name,

Object

... args)

Calls a method on a script object compiled during a previous script execution,
which is retained in the state of the

ScriptEngine

.

---

#### Method Summary

Returns an implementation of an interface using functions compiled in
the interpreter.

Returns an implementation of an interface using member functions of
a scripting object compiled in the interpreter.

Used to call top-level procedures and functions defined in scripts.

Calls a method on a script object compiled during a previous script execution,
which is retained in the state of the

ScriptEngine

.

============ METHOD DETAIL ==========

- Method Detail

- invokeMethod

```java
Object
invokeMethod​(
Object
thiz,

String
name,

Object
... args)
throws
ScriptException
,

NoSuchMethodException
```

Calls a method on a script object compiled during a previous script execution,
which is retained in the state of the

ScriptEngine

.

**Parameters:** name

- The name of the procedure to be called.
**Parameters:** thiz

- If the procedure is a member of a class
defined in the script and thiz is an instance of that class
returned by a previous execution or invocation, the named method is
called through that instance.
**Parameters:** args

- Arguments to pass to the procedure. The rules for converting
the arguments to scripting variables are implementation-specific.
**Returns:** The value returned by the procedure. The rules for converting the scripting
variable returned by the script method to a Java Object are implementation-specific.
**Throws:** ScriptException

- if an error occurs during invocation of the method.
**Throws:** NoSuchMethodException

- if method with given name or matching argument types cannot be found.
**Throws:** NullPointerException

- if the method name is null.
**Throws:** IllegalArgumentException

- if the specified thiz is null or the specified Object is
does not represent a scripting object.

- invokeFunction

```java
Object
invokeFunction​(
String
name,

Object
... args)
throws
ScriptException
,

NoSuchMethodException
```

Used to call top-level procedures and functions defined in scripts.

**Parameters:** name

- of the procedure or function to call
**Parameters:** args

- Arguments to pass to the procedure or function
**Returns:** The value returned by the procedure or function
**Throws:** ScriptException

- if an error occurs during invocation of the method.
**Throws:** NoSuchMethodException

- if method with given name or matching argument types cannot be found.
**Throws:** NullPointerException

- if method name is null.

- getInterface

```java
<T> T getInterface​(
Class
<T> clasz)
```

Returns an implementation of an interface using functions compiled in
the interpreter. The methods of the interface
may be implemented using the

invokeFunction

method.

**Type Parameters:** T

- the type of the interface to return
**Parameters:** clasz

- The

Class

object of the interface to return.
**Returns:** An instance of requested interface - null if the requested interface is unavailable,
i. e. if compiled functions in the

ScriptEngine

cannot be found matching
the ones in the requested interface.
**Throws:** IllegalArgumentException

- if the specified

Class

object
is null or is not an interface.

- getInterface

```java
<T> T getInterface​(
Object
thiz,

Class
<T> clasz)
```

Returns an implementation of an interface using member functions of
a scripting object compiled in the interpreter. The methods of the
interface may be implemented using the

invokeMethod

method.

**Type Parameters:** T

- the type of the interface to return
**Parameters:** thiz

- The scripting object whose member functions are used to implement the methods of the interface.
**Parameters:** clasz

- The

Class

object of the interface to return.
**Returns:** An instance of requested interface - null if the requested interface is unavailable,
i. e. if compiled methods in the

ScriptEngine

cannot be found matching
the ones in the requested interface.
**Throws:** IllegalArgumentException

- if the specified

Class

object
is null or is not an interface, or if the specified Object is
null or does not represent a scripting object.

Method Detail

- invokeMethod

```java
Object
invokeMethod​(
Object
thiz,

String
name,

Object
... args)
throws
ScriptException
,

NoSuchMethodException
```

Calls a method on a script object compiled during a previous script execution,
which is retained in the state of the

ScriptEngine

.

**Parameters:** name

- The name of the procedure to be called.
**Parameters:** thiz

- If the procedure is a member of a class
defined in the script and thiz is an instance of that class
returned by a previous execution or invocation, the named method is
called through that instance.
**Parameters:** args

- Arguments to pass to the procedure. The rules for converting
the arguments to scripting variables are implementation-specific.
**Returns:** The value returned by the procedure. The rules for converting the scripting
variable returned by the script method to a Java Object are implementation-specific.
**Throws:** ScriptException

- if an error occurs during invocation of the method.
**Throws:** NoSuchMethodException

- if method with given name or matching argument types cannot be found.
**Throws:** NullPointerException

- if the method name is null.
**Throws:** IllegalArgumentException

- if the specified thiz is null or the specified Object is
does not represent a scripting object.

- invokeFunction

```java
Object
invokeFunction​(
String
name,

Object
... args)
throws
ScriptException
,

NoSuchMethodException
```

Used to call top-level procedures and functions defined in scripts.

**Parameters:** name

- of the procedure or function to call
**Parameters:** args

- Arguments to pass to the procedure or function
**Returns:** The value returned by the procedure or function
**Throws:** ScriptException

- if an error occurs during invocation of the method.
**Throws:** NoSuchMethodException

- if method with given name or matching argument types cannot be found.
**Throws:** NullPointerException

- if method name is null.

- getInterface

```java
<T> T getInterface​(
Class
<T> clasz)
```

Returns an implementation of an interface using functions compiled in
the interpreter. The methods of the interface
may be implemented using the

invokeFunction

method.

**Type Parameters:** T

- the type of the interface to return
**Parameters:** clasz

- The

Class

object of the interface to return.
**Returns:** An instance of requested interface - null if the requested interface is unavailable,
i. e. if compiled functions in the

ScriptEngine

cannot be found matching
the ones in the requested interface.
**Throws:** IllegalArgumentException

- if the specified

Class

object
is null or is not an interface.

- getInterface

```java
<T> T getInterface​(
Object
thiz,

Class
<T> clasz)
```

Returns an implementation of an interface using member functions of
a scripting object compiled in the interpreter. The methods of the
interface may be implemented using the

invokeMethod

method.

**Type Parameters:** T

- the type of the interface to return
**Parameters:** thiz

- The scripting object whose member functions are used to implement the methods of the interface.
**Parameters:** clasz

- The

Class

object of the interface to return.
**Returns:** An instance of requested interface - null if the requested interface is unavailable,
i. e. if compiled methods in the

ScriptEngine

cannot be found matching
the ones in the requested interface.
**Throws:** IllegalArgumentException

- if the specified

Class

object
is null or is not an interface, or if the specified Object is
null or does not represent a scripting object.

---

#### Method Detail

invokeMethod

```java
Object
invokeMethod​(
Object
thiz,

String
name,

Object
... args)
throws
ScriptException
,

NoSuchMethodException
```

Calls a method on a script object compiled during a previous script execution,
which is retained in the state of the

ScriptEngine

.

**Parameters:** name

- The name of the procedure to be called.
**Parameters:** thiz

- If the procedure is a member of a class
defined in the script and thiz is an instance of that class
returned by a previous execution or invocation, the named method is
called through that instance.
**Parameters:** args

- Arguments to pass to the procedure. The rules for converting
the arguments to scripting variables are implementation-specific.
**Returns:** The value returned by the procedure. The rules for converting the scripting
variable returned by the script method to a Java Object are implementation-specific.
**Throws:** ScriptException

- if an error occurs during invocation of the method.
**Throws:** NoSuchMethodException

- if method with given name or matching argument types cannot be found.
**Throws:** NullPointerException

- if the method name is null.
**Throws:** IllegalArgumentException

- if the specified thiz is null or the specified Object is
does not represent a scripting object.

---

#### invokeMethod

Object

invokeMethod​(

Object

thiz,

String

name,

Object

... args)
throws

ScriptException

,

NoSuchMethodException

Calls a method on a script object compiled during a previous script execution,
which is retained in the state of the

ScriptEngine

.

invokeFunction

```java
Object
invokeFunction​(
String
name,

Object
... args)
throws
ScriptException
,

NoSuchMethodException
```

Used to call top-level procedures and functions defined in scripts.

**Parameters:** name

- of the procedure or function to call
**Parameters:** args

- Arguments to pass to the procedure or function
**Returns:** The value returned by the procedure or function
**Throws:** ScriptException

- if an error occurs during invocation of the method.
**Throws:** NoSuchMethodException

- if method with given name or matching argument types cannot be found.
**Throws:** NullPointerException

- if method name is null.

---

#### invokeFunction

Object

invokeFunction​(

String

name,

Object

... args)
throws

ScriptException

,

NoSuchMethodException

Used to call top-level procedures and functions defined in scripts.

getInterface

```java
<T> T getInterface​(
Class
<T> clasz)
```

Returns an implementation of an interface using functions compiled in
the interpreter. The methods of the interface
may be implemented using the

invokeFunction

method.

**Type Parameters:** T

- the type of the interface to return
**Parameters:** clasz

- The

Class

object of the interface to return.
**Returns:** An instance of requested interface - null if the requested interface is unavailable,
i. e. if compiled functions in the

ScriptEngine

cannot be found matching
the ones in the requested interface.
**Throws:** IllegalArgumentException

- if the specified

Class

object
is null or is not an interface.

---

#### getInterface

<T> T getInterface​(

Class

<T> clasz)

Returns an implementation of an interface using functions compiled in
the interpreter. The methods of the interface
may be implemented using the

invokeFunction

method.

getInterface

```java
<T> T getInterface​(
Object
thiz,

Class
<T> clasz)
```

Returns an implementation of an interface using member functions of
a scripting object compiled in the interpreter. The methods of the
interface may be implemented using the

invokeMethod

method.

**Type Parameters:** T

- the type of the interface to return
**Parameters:** thiz

- The scripting object whose member functions are used to implement the methods of the interface.
**Parameters:** clasz

- The

Class

object of the interface to return.
**Returns:** An instance of requested interface - null if the requested interface is unavailable,
i. e. if compiled methods in the

ScriptEngine

cannot be found matching
the ones in the requested interface.
**Throws:** IllegalArgumentException

- if the specified

Class

object
is null or is not an interface, or if the specified Object is
null or does not represent a scripting object.

---

#### getInterface

<T> T getInterface​(

Object

thiz,

Class

<T> clasz)

Returns an implementation of an interface using member functions of
a scripting object compiled in the interpreter. The methods of the
interface may be implemented using the

invokeMethod

method.

---

