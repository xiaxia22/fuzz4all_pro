# Class JSObject

**Source:** `jdk.jsobject\netscape\javascript\JSObject.html`

### Class Description

```java
public abstract class
JSObject

extends
Object
```

Allows Java code to manipulate JavaScript objects.

When a JavaScript object is passed or returned to Java code, it
is wrapped in an instance of

JSObject

. When a

JSObject

instance is passed to the JavaScript engine,
it is unwrapped back to its original JavaScript object. The

JSObject

class provides a way to invoke JavaScript
methods and examine JavaScript properties.

Any data returned from the JavaScript engine to Java is
converted to Java data types. Certain data passed to the JavaScript
engine is converted to JavaScript data types.

---

### Field Details

*No entries found.*

### Constructor Details

#### protected JSObject()

Constructs a new JSObject. Users should neither call this method nor
subclass JSObject.

---

### Method Details

#### public abstract
Object
call​(
String
methodName,

Object
... args)
throws
JSException

Calls a JavaScript method. Equivalent to
"this.methodName(args[0], args[1], ...)" in JavaScript.

**Parameters:**
- methodName

- The name of the JavaScript method to be invoked.
- args

- the Java objects passed as arguments to the method.

**Returns:**
- Result of the method.

**Throws:**
- JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### public abstract
Object
eval​(
String
s)
throws
JSException

Evaluates a JavaScript expression. The expression is a string of
JavaScript source code which will be evaluated in the context given by
"this".

**Parameters:**
- s

- The JavaScript expression.

**Returns:**
- Result of the JavaScript evaluation.

**Throws:**
- JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### public abstract
Object
getMember​(
String
name)
throws
JSException

Retrieves a named member of a JavaScript object. Equivalent to
"this.name" in JavaScript.

**Parameters:**
- name

- The name of the JavaScript property to be accessed.

**Returns:**
- The value of the propery.

**Throws:**
- JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### public abstract void setMember​(
String
name,

Object
value)
throws
JSException

Sets a named member of a JavaScript object. Equivalent to
"this.name = value" in JavaScript.

**Parameters:**
- name

- The name of the JavaScript property to be accessed.
- value

- The value of the propery.

**Throws:**
- JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### public abstract void removeMember​(
String
name)
throws
JSException

Removes a named member of a JavaScript object. Equivalent
to "delete this.name" in JavaScript.

**Parameters:**
- name

- The name of the JavaScript property to be removed.

**Throws:**
- JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### public abstract
Object
getSlot​(int index)
throws
JSException

Retrieves an indexed member of a JavaScript object. Equivalent to
"this[index]" in JavaScript.

**Parameters:**
- index

- The index of the array to be accessed.

**Returns:**
- The value of the indexed member.

**Throws:**
- JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### public abstract void setSlot​(int index,

Object
value)
throws
JSException

Sets an indexed member of a JavaScript object. Equivalent to
"this[index] = value" in JavaScript.

**Parameters:**
- index

- The index of the array to be accessed.
- value

- The value to set

**Throws:**
- JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### @Deprecated
(
since
="9")
public static
JSObject
getWindow​(
Applet
applet)
throws
JSException

Returns a JSObject for the window containing the given applet. This
method only works when the Java code is running in a browser as an
applet. The object returned may be used to access the HTML DOM directly.

**Parameters:**
- applet

- The applet.

**Returns:**
- JSObject representing the window containing the given applet or

null

if we are not connected to a browser.

**Throws:**
- JSException

- when an error is reported from the browser or
JavaScript engine or if applet is

null

---

### Additional Sections

#### Class JSObject

java.lang.Object

- netscape.javascript.JSObject

netscape.javascript.JSObject

```java
public abstract class
JSObject

extends
Object
```

Allows Java code to manipulate JavaScript objects.

When a JavaScript object is passed or returned to Java code, it
is wrapped in an instance of

JSObject

. When a

JSObject

instance is passed to the JavaScript engine,
it is unwrapped back to its original JavaScript object. The

JSObject

class provides a way to invoke JavaScript
methods and examine JavaScript properties.

Any data returned from the JavaScript engine to Java is
converted to Java data types. Certain data passed to the JavaScript
engine is converted to JavaScript data types.

public abstract class

JSObject

extends

Object

Allows Java code to manipulate JavaScript objects.

When a JavaScript object is passed or returned to Java code, it
is wrapped in an instance of

JSObject

. When a

JSObject

instance is passed to the JavaScript engine,
it is unwrapped back to its original JavaScript object. The

JSObject

class provides a way to invoke JavaScript
methods and examine JavaScript properties.

Any data returned from the JavaScript engine to Java is
converted to Java data types. Certain data passed to the JavaScript
engine is converted to JavaScript data types.

Allows Java code to manipulate JavaScript objects.

When a JavaScript object is passed or returned to Java code, it
is wrapped in an instance of

JSObject

. When a

JSObject

instance is passed to the JavaScript engine,
it is unwrapped back to its original JavaScript object. The

JSObject

class provides a way to invoke JavaScript
methods and examine JavaScript properties.

Any data returned from the JavaScript engine to Java is
converted to Java data types. Certain data passed to the JavaScript
engine is converted to JavaScript data types.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JSObject

()

Constructs a new JSObject.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract

Object

call

​(

String

methodName,

Object

... args)

Calls a JavaScript method.

abstract

Object

eval

​(

String

s)

Evaluates a JavaScript expression.

abstract

Object

getMember

​(

String

name)

Retrieves a named member of a JavaScript object.

abstract

Object

getSlot

​(int index)

Retrieves an indexed member of a JavaScript object.

static

JSObject

getWindow

​(

Applet

applet)

Deprecated.

The Applet API is deprecated.

abstract void

removeMember

​(

String

name)

Removes a named member of a JavaScript object.

abstract void

setMember

​(

String

name,

Object

value)

Sets a named member of a JavaScript object.

abstract void

setSlot

​(int index,

Object

value)

Sets an indexed member of a JavaScript object.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JSObject

()

Constructs a new JSObject.

---

#### Constructor Summary

Constructs a new JSObject.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract

Object

call

​(

String

methodName,

Object

... args)

Calls a JavaScript method.

abstract

Object

eval

​(

String

s)

Evaluates a JavaScript expression.

abstract

Object

getMember

​(

String

name)

Retrieves a named member of a JavaScript object.

abstract

Object

getSlot

​(int index)

Retrieves an indexed member of a JavaScript object.

static

JSObject

getWindow

​(

Applet

applet)

Deprecated.

The Applet API is deprecated.

abstract void

removeMember

​(

String

name)

Removes a named member of a JavaScript object.

abstract void

setMember

​(

String

name,

Object

value)

Sets a named member of a JavaScript object.

abstract void

setSlot

​(int index,

Object

value)

Sets an indexed member of a JavaScript object.

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

---

#### Method Summary

Calls a JavaScript method.

Evaluates a JavaScript expression.

Retrieves a named member of a JavaScript object.

Retrieves an indexed member of a JavaScript object.

Deprecated.

The Applet API is deprecated.

Removes a named member of a JavaScript object.

Sets a named member of a JavaScript object.

Sets an indexed member of a JavaScript object.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JSObject

```java
protected JSObject()
```

Constructs a new JSObject. Users should neither call this method nor
subclass JSObject.

============ METHOD DETAIL ==========

- Method Detail

- call

```java
public abstract
Object
call​(
String
methodName,

Object
... args)
throws
JSException
```

Calls a JavaScript method. Equivalent to
"this.methodName(args[0], args[1], ...)" in JavaScript.

**Parameters:** methodName

- The name of the JavaScript method to be invoked.
**Parameters:** args

- the Java objects passed as arguments to the method.
**Returns:** Result of the method.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- eval

```java
public abstract
Object
eval​(
String
s)
throws
JSException
```

Evaluates a JavaScript expression. The expression is a string of
JavaScript source code which will be evaluated in the context given by
"this".

**Parameters:** s

- The JavaScript expression.
**Returns:** Result of the JavaScript evaluation.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- getMember

```java
public abstract
Object
getMember​(
String
name)
throws
JSException
```

Retrieves a named member of a JavaScript object. Equivalent to
"this.name" in JavaScript.

**Parameters:** name

- The name of the JavaScript property to be accessed.
**Returns:** The value of the propery.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- setMember

```java
public abstract void setMember​(
String
name,

Object
value)
throws
JSException
```

Sets a named member of a JavaScript object. Equivalent to
"this.name = value" in JavaScript.

**Parameters:** name

- The name of the JavaScript property to be accessed.
**Parameters:** value

- The value of the propery.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- removeMember

```java
public abstract void removeMember​(
String
name)
throws
JSException
```

Removes a named member of a JavaScript object. Equivalent
to "delete this.name" in JavaScript.

**Parameters:** name

- The name of the JavaScript property to be removed.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- getSlot

```java
public abstract
Object
getSlot​(int index)
throws
JSException
```

Retrieves an indexed member of a JavaScript object. Equivalent to
"this[index]" in JavaScript.

**Parameters:** index

- The index of the array to be accessed.
**Returns:** The value of the indexed member.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- setSlot

```java
public abstract void setSlot​(int index,

Object
value)
throws
JSException
```

Sets an indexed member of a JavaScript object. Equivalent to
"this[index] = value" in JavaScript.

**Parameters:** index

- The index of the array to be accessed.
**Parameters:** value

- The value to set
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- getWindow

```java
@Deprecated
(
since
="9")
public static
JSObject
getWindow​(
Applet
applet)
throws
JSException
```

Deprecated.

The Applet API is deprecated. See the

java.applet package documentation

for further information.

Returns a JSObject for the window containing the given applet. This
method only works when the Java code is running in a browser as an
applet. The object returned may be used to access the HTML DOM directly.

**Parameters:** applet

- The applet.
**Returns:** JSObject representing the window containing the given applet or

null

if we are not connected to a browser.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine or if applet is

null

Constructor Detail

- JSObject

```java
protected JSObject()
```

Constructs a new JSObject. Users should neither call this method nor
subclass JSObject.

---

#### Constructor Detail

JSObject

```java
protected JSObject()
```

Constructs a new JSObject. Users should neither call this method nor
subclass JSObject.

---

#### JSObject

protected JSObject()

Constructs a new JSObject. Users should neither call this method nor
subclass JSObject.

Method Detail

- call

```java
public abstract
Object
call​(
String
methodName,

Object
... args)
throws
JSException
```

Calls a JavaScript method. Equivalent to
"this.methodName(args[0], args[1], ...)" in JavaScript.

**Parameters:** methodName

- The name of the JavaScript method to be invoked.
**Parameters:** args

- the Java objects passed as arguments to the method.
**Returns:** Result of the method.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- eval

```java
public abstract
Object
eval​(
String
s)
throws
JSException
```

Evaluates a JavaScript expression. The expression is a string of
JavaScript source code which will be evaluated in the context given by
"this".

**Parameters:** s

- The JavaScript expression.
**Returns:** Result of the JavaScript evaluation.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- getMember

```java
public abstract
Object
getMember​(
String
name)
throws
JSException
```

Retrieves a named member of a JavaScript object. Equivalent to
"this.name" in JavaScript.

**Parameters:** name

- The name of the JavaScript property to be accessed.
**Returns:** The value of the propery.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- setMember

```java
public abstract void setMember​(
String
name,

Object
value)
throws
JSException
```

Sets a named member of a JavaScript object. Equivalent to
"this.name = value" in JavaScript.

**Parameters:** name

- The name of the JavaScript property to be accessed.
**Parameters:** value

- The value of the propery.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- removeMember

```java
public abstract void removeMember​(
String
name)
throws
JSException
```

Removes a named member of a JavaScript object. Equivalent
to "delete this.name" in JavaScript.

**Parameters:** name

- The name of the JavaScript property to be removed.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- getSlot

```java
public abstract
Object
getSlot​(int index)
throws
JSException
```

Retrieves an indexed member of a JavaScript object. Equivalent to
"this[index]" in JavaScript.

**Parameters:** index

- The index of the array to be accessed.
**Returns:** The value of the indexed member.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- setSlot

```java
public abstract void setSlot​(int index,

Object
value)
throws
JSException
```

Sets an indexed member of a JavaScript object. Equivalent to
"this[index] = value" in JavaScript.

**Parameters:** index

- The index of the array to be accessed.
**Parameters:** value

- The value to set
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

- getWindow

```java
@Deprecated
(
since
="9")
public static
JSObject
getWindow​(
Applet
applet)
throws
JSException
```

Deprecated.

The Applet API is deprecated. See the

java.applet package documentation

for further information.

Returns a JSObject for the window containing the given applet. This
method only works when the Java code is running in a browser as an
applet. The object returned may be used to access the HTML DOM directly.

**Parameters:** applet

- The applet.
**Returns:** JSObject representing the window containing the given applet or

null

if we are not connected to a browser.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine or if applet is

null

---

#### Method Detail

call

```java
public abstract
Object
call​(
String
methodName,

Object
... args)
throws
JSException
```

Calls a JavaScript method. Equivalent to
"this.methodName(args[0], args[1], ...)" in JavaScript.

**Parameters:** methodName

- The name of the JavaScript method to be invoked.
**Parameters:** args

- the Java objects passed as arguments to the method.
**Returns:** Result of the method.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### call

public abstract

Object

call​(

String

methodName,

Object

... args)
throws

JSException

Calls a JavaScript method. Equivalent to
"this.methodName(args[0], args[1], ...)" in JavaScript.

eval

```java
public abstract
Object
eval​(
String
s)
throws
JSException
```

Evaluates a JavaScript expression. The expression is a string of
JavaScript source code which will be evaluated in the context given by
"this".

**Parameters:** s

- The JavaScript expression.
**Returns:** Result of the JavaScript evaluation.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### eval

public abstract

Object

eval​(

String

s)
throws

JSException

Evaluates a JavaScript expression. The expression is a string of
JavaScript source code which will be evaluated in the context given by
"this".

getMember

```java
public abstract
Object
getMember​(
String
name)
throws
JSException
```

Retrieves a named member of a JavaScript object. Equivalent to
"this.name" in JavaScript.

**Parameters:** name

- The name of the JavaScript property to be accessed.
**Returns:** The value of the propery.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### getMember

public abstract

Object

getMember​(

String

name)
throws

JSException

Retrieves a named member of a JavaScript object. Equivalent to
"this.name" in JavaScript.

setMember

```java
public abstract void setMember​(
String
name,

Object
value)
throws
JSException
```

Sets a named member of a JavaScript object. Equivalent to
"this.name = value" in JavaScript.

**Parameters:** name

- The name of the JavaScript property to be accessed.
**Parameters:** value

- The value of the propery.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### setMember

public abstract void setMember​(

String

name,

Object

value)
throws

JSException

Sets a named member of a JavaScript object. Equivalent to
"this.name = value" in JavaScript.

removeMember

```java
public abstract void removeMember​(
String
name)
throws
JSException
```

Removes a named member of a JavaScript object. Equivalent
to "delete this.name" in JavaScript.

**Parameters:** name

- The name of the JavaScript property to be removed.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### removeMember

public abstract void removeMember​(

String

name)
throws

JSException

Removes a named member of a JavaScript object. Equivalent
to "delete this.name" in JavaScript.

getSlot

```java
public abstract
Object
getSlot​(int index)
throws
JSException
```

Retrieves an indexed member of a JavaScript object. Equivalent to
"this[index]" in JavaScript.

**Parameters:** index

- The index of the array to be accessed.
**Returns:** The value of the indexed member.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### getSlot

public abstract

Object

getSlot​(int index)
throws

JSException

Retrieves an indexed member of a JavaScript object. Equivalent to
"this[index]" in JavaScript.

setSlot

```java
public abstract void setSlot​(int index,

Object
value)
throws
JSException
```

Sets an indexed member of a JavaScript object. Equivalent to
"this[index] = value" in JavaScript.

**Parameters:** index

- The index of the array to be accessed.
**Parameters:** value

- The value to set
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine.

---

#### setSlot

public abstract void setSlot​(int index,

Object

value)
throws

JSException

Sets an indexed member of a JavaScript object. Equivalent to
"this[index] = value" in JavaScript.

getWindow

```java
@Deprecated
(
since
="9")
public static
JSObject
getWindow​(
Applet
applet)
throws
JSException
```

Deprecated.

The Applet API is deprecated. See the

java.applet package documentation

for further information.

Returns a JSObject for the window containing the given applet. This
method only works when the Java code is running in a browser as an
applet. The object returned may be used to access the HTML DOM directly.

**Parameters:** applet

- The applet.
**Returns:** JSObject representing the window containing the given applet or

null

if we are not connected to a browser.
**Throws:** JSException

- when an error is reported from the browser or
JavaScript engine or if applet is

null

---

#### getWindow

@Deprecated

(

since

="9")
public static

JSObject

getWindow​(

Applet

applet)
throws

JSException

Returns a JSObject for the window containing the given applet. This
method only works when the Java code is running in a browser as an
applet. The object returned may be used to access the HTML DOM directly.

---

