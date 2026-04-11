# Class AbstractScriptEngine

**Source:** `java.scripting\javax\script\AbstractScriptEngine.html`

### Class Description

```java
public abstract class
AbstractScriptEngine

extends
Object

implements
ScriptEngine
```

Provides a standard implementation for several of the variants of the

eval

method.

eval(Reader)

eval(String)

eval(String, Bindings)

eval(Reader, Bindings)

are implemented using the abstract methods

eval(Reader,ScriptContext)

or

eval(String, ScriptContext)

with a

SimpleScriptContext

.

A

SimpleScriptContext

is used as the default

ScriptContext

of the

AbstractScriptEngine

..

**All Implemented Interfaces:** ScriptEngine

---

### Field Details

#### protected
ScriptContext
context

The default

ScriptContext

of this

AbstractScriptEngine

.

---

### Constructor Details

#### public AbstractScriptEngine()

Creates a new instance of AbstractScriptEngine using a

SimpleScriptContext

as its default

ScriptContext

.

---

#### public AbstractScriptEngine​(
Bindings
n)

Creates a new instance using the specified

Bindings

as the

ENGINE_SCOPE

Bindings

in the protected

context

field.

**Parameters:**
- n

- The specified

Bindings

.

**Throws:**
- NullPointerException

- if n is null.

---

### Method Details

#### public void setContext​(
ScriptContext
ctxt)

Sets the value of the protected

context

field to the specified

ScriptContext

.

**Specified by:**
- setContext

in interface

ScriptEngine

**Parameters:**
- ctxt

- The specified

ScriptContext

.

**Throws:**
- NullPointerException

- if ctxt is null.

---

#### public
ScriptContext
getContext()

Returns the value of the protected

context

field.

**Specified by:**
- getContext

in interface

ScriptEngine

**Returns:**
- The value of the protected

context

field.

---

#### public
Bindings
getBindings​(int scope)

Returns the

Bindings

with the specified scope value in
the protected

context

field.

**Specified by:**
- getBindings

in interface

ScriptEngine

**Parameters:**
- scope

- The specified scope

**Returns:**
- The corresponding

Bindings

.

**Throws:**
- IllegalArgumentException

- if the value of scope is
invalid for the type the protected

context

field.

---

#### public void setBindings​(
Bindings
bindings,
int scope)

Sets the

Bindings

with the corresponding scope value in the

context

field.

**Specified by:**
- setBindings

in interface

ScriptEngine

**Parameters:**
- bindings

- The specified

Bindings

.
- scope

- The specified scope.

**Throws:**
- IllegalArgumentException

- if the value of scope is
invalid for the type the

context

field.
- NullPointerException

- if the bindings is null and the scope is

ScriptContext.ENGINE_SCOPE

---

#### public void put​(
String
key,

Object
value)

Sets the specified value with the specified key in the

ENGINE_SCOPE

Bindings

of the protected

context

field.

**Specified by:**
- put

in interface

ScriptEngine

**Parameters:**
- key

- The specified key.
- value

- The specified value.

**Throws:**
- NullPointerException

- if key is null.
- IllegalArgumentException

- if key is empty.

---

#### public
Object
get​(
String
key)

Gets the value for the specified key in the

ENGINE_SCOPE

of the
protected

context

field.

**Specified by:**
- get

in interface

ScriptEngine

**Parameters:**
- key

- The key whose value is to be returned

**Returns:**
- The value for the specified key.

**Throws:**
- NullPointerException

- if key is null.
- IllegalArgumentException

- if key is empty.

---

#### public
Object
eval​(
Reader
reader,

Bindings
bindings)
throws
ScriptException

eval(Reader, Bindings)

calls the abstract

eval(Reader, ScriptContext)

method, passing it a

ScriptContext

whose Reader, Writers and Bindings for scopes other that

ENGINE_SCOPE

are identical to those members of the protected

context

field. The specified

Bindings

is used instead of the

ENGINE_SCOPE

Bindings

of the

context

field.

**Specified by:**
- eval

in interface

ScriptEngine

**Parameters:**
- reader

- A

Reader

containing the source of the script.
- bindings

- A

Bindings

to use for the

ENGINE_SCOPE

while the script executes.

**Returns:**
- The return value from

eval(Reader, ScriptContext)

**Throws:**
- ScriptException

- if an error occurs in script.
- NullPointerException

- if any of the parameters is null.

---

#### public
Object
eval​(
String
script,

Bindings
bindings)
throws
ScriptException

Same as

eval(Reader, Bindings)

except that the abstract

eval(String, ScriptContext)

is used.

**Specified by:**
- eval

in interface

ScriptEngine

**Parameters:**
- script

- A

String

containing the source of the script.
- bindings

- A

Bindings

to use as the

ENGINE_SCOPE

while the script executes.

**Returns:**
- The return value from

eval(String, ScriptContext)

**Throws:**
- ScriptException

- if an error occurs in script.
- NullPointerException

- if any of the parameters is null.

---

#### public
Object
eval​(
Reader
reader)
throws
ScriptException

eval(Reader)

calls the abstract

eval(Reader, ScriptContext)

passing the value of the

context

field.

**Specified by:**
- eval

in interface

ScriptEngine

**Parameters:**
- reader

- A

Reader

containing the source of the script.

**Returns:**
- The return value from

eval(Reader, ScriptContext)

**Throws:**
- ScriptException

- if an error occurs in script.
- NullPointerException

- if any of the parameters is null.

---

#### public
Object
eval​(
String
script)
throws
ScriptException

Same as

eval(Reader)

except that the abstract

eval(String, ScriptContext)

is used.

**Specified by:**
- eval

in interface

ScriptEngine

**Parameters:**
- script

- A

String

containing the source of the script.

**Returns:**
- The return value from

eval(String, ScriptContext)

**Throws:**
- ScriptException

- if an error occurs in script.
- NullPointerException

- if any of the parameters is null.

---

#### protected
ScriptContext
getScriptContext​(
Bindings
nn)

Returns a

SimpleScriptContext

. The

SimpleScriptContext

:

- Uses the specified

Bindings

for its

ENGINE_SCOPE
- Uses the

Bindings

returned by the abstract

getGlobalScope

method as its

GLOBAL_SCOPE
- Uses the Reader and Writer in the default

ScriptContext

of this

ScriptEngine

A

SimpleScriptContext

returned by this method is used to implement eval methods
using the abstract

eval(Reader,Bindings)

and

eval(String,Bindings)

versions.

**Parameters:**
- nn

- Bindings to use for the

ENGINE_SCOPE

**Returns:**
- The

SimpleScriptContext

---

### Additional Sections

#### Class AbstractScriptEngine

java.lang.Object

- javax.script.AbstractScriptEngine

javax.script.AbstractScriptEngine

**All Implemented Interfaces:** ScriptEngine

**Direct Known Subclasses:** NashornScriptEngine

```java
public abstract class
AbstractScriptEngine

extends
Object

implements
ScriptEngine
```

Provides a standard implementation for several of the variants of the

eval

method.

eval(Reader)

eval(String)

eval(String, Bindings)

eval(Reader, Bindings)

are implemented using the abstract methods

eval(Reader,ScriptContext)

or

eval(String, ScriptContext)

with a

SimpleScriptContext

.

A

SimpleScriptContext

is used as the default

ScriptContext

of the

AbstractScriptEngine

..

**Since:** 1.6

public abstract class

AbstractScriptEngine

extends

Object

implements

ScriptEngine

Provides a standard implementation for several of the variants of the

eval

method.

eval(Reader)

eval(String)

eval(String, Bindings)

eval(Reader, Bindings)

are implemented using the abstract methods

eval(Reader,ScriptContext)

or

eval(String, ScriptContext)

with a

SimpleScriptContext

.

A

SimpleScriptContext

is used as the default

ScriptContext

of the

AbstractScriptEngine

..

eval(String)

eval(String, Bindings)

eval(Reader, Bindings)

are implemented using the abstract methods

eval(Reader,ScriptContext)

or

eval(String, ScriptContext)

with a

SimpleScriptContext

.

A

SimpleScriptContext

is used as the default

ScriptContext

of the

AbstractScriptEngine

..

eval(String, Bindings)

eval(Reader, Bindings)

are implemented using the abstract methods

eval(Reader,ScriptContext)

or

eval(String, ScriptContext)

with a

SimpleScriptContext

.

A

SimpleScriptContext

is used as the default

ScriptContext

of the

AbstractScriptEngine

..

eval(Reader, Bindings)

are implemented using the abstract methods

eval(Reader,ScriptContext)

or

eval(String, ScriptContext)

with a

SimpleScriptContext

.

A

SimpleScriptContext

is used as the default

ScriptContext

of the

AbstractScriptEngine

..

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ScriptContext

context

The default

ScriptContext

of this

AbstractScriptEngine

.

- Fields declared in interface javax.script.

ScriptEngine

ARGV

,

ENGINE

,

ENGINE_VERSION

,

FILENAME

,

LANGUAGE

,

LANGUAGE_VERSION

,

NAME

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractScriptEngine

()

Creates a new instance of AbstractScriptEngine using a

SimpleScriptContext

as its default

ScriptContext

.

AbstractScriptEngine

​(

Bindings

n)

Creates a new instance using the specified

Bindings

as the

ENGINE_SCOPE

Bindings

in the protected

context

field.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

eval

​(

Reader

reader)

eval(Reader)

calls the abstract

eval(Reader, ScriptContext)

passing the value of the

context

field.

Object

eval

​(

Reader

reader,

Bindings

bindings)

eval(Reader, Bindings)

calls the abstract

eval(Reader, ScriptContext)

method, passing it a

ScriptContext

whose Reader, Writers and Bindings for scopes other that

ENGINE_SCOPE

are identical to those members of the protected

context

field.

Object

eval

​(

String

script)

Same as

eval(Reader)

except that the abstract

eval(String, ScriptContext)

is used.

Object

eval

​(

String

script,

Bindings

bindings)

Same as

eval(Reader, Bindings)

except that the abstract

eval(String, ScriptContext)

is used.

Object

get

​(

String

key)

Gets the value for the specified key in the

ENGINE_SCOPE

of the
protected

context

field.

Bindings

getBindings

​(int scope)

Returns the

Bindings

with the specified scope value in
the protected

context

field.

ScriptContext

getContext

()

Returns the value of the protected

context

field.

protected

ScriptContext

getScriptContext

​(

Bindings

nn)

Returns a

SimpleScriptContext

.

void

put

​(

String

key,

Object

value)

Sets the specified value with the specified key in the

ENGINE_SCOPE

Bindings

of the protected

context

field.

void

setBindings

​(

Bindings

bindings,
int scope)

Sets the

Bindings

with the corresponding scope value in the

context

field.

void

setContext

​(

ScriptContext

ctxt)

Sets the value of the protected

context

field to the specified

ScriptContext

.

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

- Methods declared in interface javax.script.

ScriptEngine

createBindings

,

eval

,

eval

,

getFactory

Field Summary

Fields

Modifier and Type

Field

Description

protected

ScriptContext

context

The default

ScriptContext

of this

AbstractScriptEngine

.

- Fields declared in interface javax.script.

ScriptEngine

ARGV

,

ENGINE

,

ENGINE_VERSION

,

FILENAME

,

LANGUAGE

,

LANGUAGE_VERSION

,

NAME

---

#### Field Summary

The default

ScriptContext

of this

AbstractScriptEngine

.

Fields declared in interface javax.script.

ScriptEngine

ARGV

,

ENGINE

,

ENGINE_VERSION

,

FILENAME

,

LANGUAGE

,

LANGUAGE_VERSION

,

NAME

---

#### Fields declared in interface javax.script. ScriptEngine

Constructor Summary

Constructors

Constructor

Description

AbstractScriptEngine

()

Creates a new instance of AbstractScriptEngine using a

SimpleScriptContext

as its default

ScriptContext

.

AbstractScriptEngine

​(

Bindings

n)

Creates a new instance using the specified

Bindings

as the

ENGINE_SCOPE

Bindings

in the protected

context

field.

---

#### Constructor Summary

Creates a new instance of AbstractScriptEngine using a

SimpleScriptContext

as its default

ScriptContext

.

Creates a new instance using the specified

Bindings

as the

ENGINE_SCOPE

Bindings

in the protected

context

field.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

eval

​(

Reader

reader)

eval(Reader)

calls the abstract

eval(Reader, ScriptContext)

passing the value of the

context

field.

Object

eval

​(

Reader

reader,

Bindings

bindings)

eval(Reader, Bindings)

calls the abstract

eval(Reader, ScriptContext)

method, passing it a

ScriptContext

whose Reader, Writers and Bindings for scopes other that

ENGINE_SCOPE

are identical to those members of the protected

context

field.

Object

eval

​(

String

script)

Same as

eval(Reader)

except that the abstract

eval(String, ScriptContext)

is used.

Object

eval

​(

String

script,

Bindings

bindings)

Same as

eval(Reader, Bindings)

except that the abstract

eval(String, ScriptContext)

is used.

Object

get

​(

String

key)

Gets the value for the specified key in the

ENGINE_SCOPE

of the
protected

context

field.

Bindings

getBindings

​(int scope)

Returns the

Bindings

with the specified scope value in
the protected

context

field.

ScriptContext

getContext

()

Returns the value of the protected

context

field.

protected

ScriptContext

getScriptContext

​(

Bindings

nn)

Returns a

SimpleScriptContext

.

void

put

​(

String

key,

Object

value)

Sets the specified value with the specified key in the

ENGINE_SCOPE

Bindings

of the protected

context

field.

void

setBindings

​(

Bindings

bindings,
int scope)

Sets the

Bindings

with the corresponding scope value in the

context

field.

void

setContext

​(

ScriptContext

ctxt)

Sets the value of the protected

context

field to the specified

ScriptContext

.

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

- Methods declared in interface javax.script.

ScriptEngine

createBindings

,

eval

,

eval

,

getFactory

---

#### Method Summary

eval(Reader)

calls the abstract

eval(Reader, ScriptContext)

passing the value of the

context

field.

eval(Reader, Bindings)

calls the abstract

eval(Reader, ScriptContext)

method, passing it a

ScriptContext

whose Reader, Writers and Bindings for scopes other that

ENGINE_SCOPE

are identical to those members of the protected

context

field.

Same as

eval(Reader)

except that the abstract

eval(String, ScriptContext)

is used.

Same as

eval(Reader, Bindings)

except that the abstract

eval(String, ScriptContext)

is used.

Gets the value for the specified key in the

ENGINE_SCOPE

of the
protected

context

field.

Returns the

Bindings

with the specified scope value in
the protected

context

field.

Returns the value of the protected

context

field.

Returns a

SimpleScriptContext

.

Sets the specified value with the specified key in the

ENGINE_SCOPE

Bindings

of the protected

context

field.

Sets the

Bindings

with the corresponding scope value in the

context

field.

Sets the value of the protected

context

field to the specified

ScriptContext

.

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

Methods declared in interface javax.script.

ScriptEngine

createBindings

,

eval

,

eval

,

getFactory

---

#### Methods declared in interface javax.script. ScriptEngine

============ FIELD DETAIL ===========

- Field Detail

- context

```java
protected
ScriptContext
context
```

The default

ScriptContext

of this

AbstractScriptEngine

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractScriptEngine

```java
public AbstractScriptEngine()
```

Creates a new instance of AbstractScriptEngine using a

SimpleScriptContext

as its default

ScriptContext

.

- AbstractScriptEngine

```java
public AbstractScriptEngine​(
Bindings
n)
```

Creates a new instance using the specified

Bindings

as the

ENGINE_SCOPE

Bindings

in the protected

context

field.

**Parameters:** n

- The specified

Bindings

.
**Throws:** NullPointerException

- if n is null.

============ METHOD DETAIL ==========

- Method Detail

- setContext

```java
public void setContext​(
ScriptContext
ctxt)
```

Sets the value of the protected

context

field to the specified

ScriptContext

.

**Specified by:** setContext

in interface

ScriptEngine
**Parameters:** ctxt

- The specified

ScriptContext

.
**Throws:** NullPointerException

- if ctxt is null.

- getContext

```java
public
ScriptContext
getContext()
```

Returns the value of the protected

context

field.

**Specified by:** getContext

in interface

ScriptEngine
**Returns:** The value of the protected

context

field.

- getBindings

```java
public
Bindings
getBindings​(int scope)
```

Returns the

Bindings

with the specified scope value in
the protected

context

field.

**Specified by:** getBindings

in interface

ScriptEngine
**Parameters:** scope

- The specified scope
**Returns:** The corresponding

Bindings

.
**Throws:** IllegalArgumentException

- if the value of scope is
invalid for the type the protected

context

field.

- setBindings

```java
public void setBindings​(
Bindings
bindings,
int scope)
```

Sets the

Bindings

with the corresponding scope value in the

context

field.

**Specified by:** setBindings

in interface

ScriptEngine
**Parameters:** bindings

- The specified

Bindings

.
**Parameters:** scope

- The specified scope.
**Throws:** IllegalArgumentException

- if the value of scope is
invalid for the type the

context

field.
**Throws:** NullPointerException

- if the bindings is null and the scope is

ScriptContext.ENGINE_SCOPE

- put

```java
public void put​(
String
key,

Object
value)
```

Sets the specified value with the specified key in the

ENGINE_SCOPE

Bindings

of the protected

context

field.

**Specified by:** put

in interface

ScriptEngine
**Parameters:** key

- The specified key.
**Parameters:** value

- The specified value.
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

- get

```java
public
Object
get​(
String
key)
```

Gets the value for the specified key in the

ENGINE_SCOPE

of the
protected

context

field.

**Specified by:** get

in interface

ScriptEngine
**Parameters:** key

- The key whose value is to be returned
**Returns:** The value for the specified key.
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

- eval

```java
public
Object
eval​(
Reader
reader,

Bindings
bindings)
throws
ScriptException
```

eval(Reader, Bindings)

calls the abstract

eval(Reader, ScriptContext)

method, passing it a

ScriptContext

whose Reader, Writers and Bindings for scopes other that

ENGINE_SCOPE

are identical to those members of the protected

context

field. The specified

Bindings

is used instead of the

ENGINE_SCOPE

Bindings

of the

context

field.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** reader

- A

Reader

containing the source of the script.
**Parameters:** bindings

- A

Bindings

to use for the

ENGINE_SCOPE

while the script executes.
**Returns:** The return value from

eval(Reader, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

- eval

```java
public
Object
eval​(
String
script,

Bindings
bindings)
throws
ScriptException
```

Same as

eval(Reader, Bindings)

except that the abstract

eval(String, ScriptContext)

is used.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** script

- A

String

containing the source of the script.
**Parameters:** bindings

- A

Bindings

to use as the

ENGINE_SCOPE

while the script executes.
**Returns:** The return value from

eval(String, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

- eval

```java
public
Object
eval​(
Reader
reader)
throws
ScriptException
```

eval(Reader)

calls the abstract

eval(Reader, ScriptContext)

passing the value of the

context

field.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** reader

- A

Reader

containing the source of the script.
**Returns:** The return value from

eval(Reader, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

- eval

```java
public
Object
eval​(
String
script)
throws
ScriptException
```

Same as

eval(Reader)

except that the abstract

eval(String, ScriptContext)

is used.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** script

- A

String

containing the source of the script.
**Returns:** The return value from

eval(String, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

- getScriptContext

```java
protected
ScriptContext
getScriptContext​(
Bindings
nn)
```

Returns a

SimpleScriptContext

. The

SimpleScriptContext

:

- Uses the specified

Bindings

for its

ENGINE_SCOPE
- Uses the

Bindings

returned by the abstract

getGlobalScope

method as its

GLOBAL_SCOPE
- Uses the Reader and Writer in the default

ScriptContext

of this

ScriptEngine

A

SimpleScriptContext

returned by this method is used to implement eval methods
using the abstract

eval(Reader,Bindings)

and

eval(String,Bindings)

versions.

**Parameters:** nn

- Bindings to use for the

ENGINE_SCOPE
**Returns:** The

SimpleScriptContext

Field Detail

- context

```java
protected
ScriptContext
context
```

The default

ScriptContext

of this

AbstractScriptEngine

.

---

#### Field Detail

context

```java
protected
ScriptContext
context
```

The default

ScriptContext

of this

AbstractScriptEngine

.

---

#### context

protected

ScriptContext

context

The default

ScriptContext

of this

AbstractScriptEngine

.

Constructor Detail

- AbstractScriptEngine

```java
public AbstractScriptEngine()
```

Creates a new instance of AbstractScriptEngine using a

SimpleScriptContext

as its default

ScriptContext

.

- AbstractScriptEngine

```java
public AbstractScriptEngine​(
Bindings
n)
```

Creates a new instance using the specified

Bindings

as the

ENGINE_SCOPE

Bindings

in the protected

context

field.

**Parameters:** n

- The specified

Bindings

.
**Throws:** NullPointerException

- if n is null.

---

#### Constructor Detail

AbstractScriptEngine

```java
public AbstractScriptEngine()
```

Creates a new instance of AbstractScriptEngine using a

SimpleScriptContext

as its default

ScriptContext

.

---

#### AbstractScriptEngine

public AbstractScriptEngine()

Creates a new instance of AbstractScriptEngine using a

SimpleScriptContext

as its default

ScriptContext

.

AbstractScriptEngine

```java
public AbstractScriptEngine​(
Bindings
n)
```

Creates a new instance using the specified

Bindings

as the

ENGINE_SCOPE

Bindings

in the protected

context

field.

**Parameters:** n

- The specified

Bindings

.
**Throws:** NullPointerException

- if n is null.

---

#### AbstractScriptEngine

public AbstractScriptEngine​(

Bindings

n)

Creates a new instance using the specified

Bindings

as the

ENGINE_SCOPE

Bindings

in the protected

context

field.

Method Detail

- setContext

```java
public void setContext​(
ScriptContext
ctxt)
```

Sets the value of the protected

context

field to the specified

ScriptContext

.

**Specified by:** setContext

in interface

ScriptEngine
**Parameters:** ctxt

- The specified

ScriptContext

.
**Throws:** NullPointerException

- if ctxt is null.

- getContext

```java
public
ScriptContext
getContext()
```

Returns the value of the protected

context

field.

**Specified by:** getContext

in interface

ScriptEngine
**Returns:** The value of the protected

context

field.

- getBindings

```java
public
Bindings
getBindings​(int scope)
```

Returns the

Bindings

with the specified scope value in
the protected

context

field.

**Specified by:** getBindings

in interface

ScriptEngine
**Parameters:** scope

- The specified scope
**Returns:** The corresponding

Bindings

.
**Throws:** IllegalArgumentException

- if the value of scope is
invalid for the type the protected

context

field.

- setBindings

```java
public void setBindings​(
Bindings
bindings,
int scope)
```

Sets the

Bindings

with the corresponding scope value in the

context

field.

**Specified by:** setBindings

in interface

ScriptEngine
**Parameters:** bindings

- The specified

Bindings

.
**Parameters:** scope

- The specified scope.
**Throws:** IllegalArgumentException

- if the value of scope is
invalid for the type the

context

field.
**Throws:** NullPointerException

- if the bindings is null and the scope is

ScriptContext.ENGINE_SCOPE

- put

```java
public void put​(
String
key,

Object
value)
```

Sets the specified value with the specified key in the

ENGINE_SCOPE

Bindings

of the protected

context

field.

**Specified by:** put

in interface

ScriptEngine
**Parameters:** key

- The specified key.
**Parameters:** value

- The specified value.
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

- get

```java
public
Object
get​(
String
key)
```

Gets the value for the specified key in the

ENGINE_SCOPE

of the
protected

context

field.

**Specified by:** get

in interface

ScriptEngine
**Parameters:** key

- The key whose value is to be returned
**Returns:** The value for the specified key.
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

- eval

```java
public
Object
eval​(
Reader
reader,

Bindings
bindings)
throws
ScriptException
```

eval(Reader, Bindings)

calls the abstract

eval(Reader, ScriptContext)

method, passing it a

ScriptContext

whose Reader, Writers and Bindings for scopes other that

ENGINE_SCOPE

are identical to those members of the protected

context

field. The specified

Bindings

is used instead of the

ENGINE_SCOPE

Bindings

of the

context

field.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** reader

- A

Reader

containing the source of the script.
**Parameters:** bindings

- A

Bindings

to use for the

ENGINE_SCOPE

while the script executes.
**Returns:** The return value from

eval(Reader, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

- eval

```java
public
Object
eval​(
String
script,

Bindings
bindings)
throws
ScriptException
```

Same as

eval(Reader, Bindings)

except that the abstract

eval(String, ScriptContext)

is used.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** script

- A

String

containing the source of the script.
**Parameters:** bindings

- A

Bindings

to use as the

ENGINE_SCOPE

while the script executes.
**Returns:** The return value from

eval(String, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

- eval

```java
public
Object
eval​(
Reader
reader)
throws
ScriptException
```

eval(Reader)

calls the abstract

eval(Reader, ScriptContext)

passing the value of the

context

field.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** reader

- A

Reader

containing the source of the script.
**Returns:** The return value from

eval(Reader, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

- eval

```java
public
Object
eval​(
String
script)
throws
ScriptException
```

Same as

eval(Reader)

except that the abstract

eval(String, ScriptContext)

is used.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** script

- A

String

containing the source of the script.
**Returns:** The return value from

eval(String, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

- getScriptContext

```java
protected
ScriptContext
getScriptContext​(
Bindings
nn)
```

Returns a

SimpleScriptContext

. The

SimpleScriptContext

:

- Uses the specified

Bindings

for its

ENGINE_SCOPE
- Uses the

Bindings

returned by the abstract

getGlobalScope

method as its

GLOBAL_SCOPE
- Uses the Reader and Writer in the default

ScriptContext

of this

ScriptEngine

A

SimpleScriptContext

returned by this method is used to implement eval methods
using the abstract

eval(Reader,Bindings)

and

eval(String,Bindings)

versions.

**Parameters:** nn

- Bindings to use for the

ENGINE_SCOPE
**Returns:** The

SimpleScriptContext

---

#### Method Detail

setContext

```java
public void setContext​(
ScriptContext
ctxt)
```

Sets the value of the protected

context

field to the specified

ScriptContext

.

**Specified by:** setContext

in interface

ScriptEngine
**Parameters:** ctxt

- The specified

ScriptContext

.
**Throws:** NullPointerException

- if ctxt is null.

---

#### setContext

public void setContext​(

ScriptContext

ctxt)

Sets the value of the protected

context

field to the specified

ScriptContext

.

getContext

```java
public
ScriptContext
getContext()
```

Returns the value of the protected

context

field.

**Specified by:** getContext

in interface

ScriptEngine
**Returns:** The value of the protected

context

field.

---

#### getContext

public

ScriptContext

getContext()

Returns the value of the protected

context

field.

getBindings

```java
public
Bindings
getBindings​(int scope)
```

Returns the

Bindings

with the specified scope value in
the protected

context

field.

**Specified by:** getBindings

in interface

ScriptEngine
**Parameters:** scope

- The specified scope
**Returns:** The corresponding

Bindings

.
**Throws:** IllegalArgumentException

- if the value of scope is
invalid for the type the protected

context

field.

---

#### getBindings

public

Bindings

getBindings​(int scope)

Returns the

Bindings

with the specified scope value in
the protected

context

field.

setBindings

```java
public void setBindings​(
Bindings
bindings,
int scope)
```

Sets the

Bindings

with the corresponding scope value in the

context

field.

**Specified by:** setBindings

in interface

ScriptEngine
**Parameters:** bindings

- The specified

Bindings

.
**Parameters:** scope

- The specified scope.
**Throws:** IllegalArgumentException

- if the value of scope is
invalid for the type the

context

field.
**Throws:** NullPointerException

- if the bindings is null and the scope is

ScriptContext.ENGINE_SCOPE

---

#### setBindings

public void setBindings​(

Bindings

bindings,
int scope)

Sets the

Bindings

with the corresponding scope value in the

context

field.

put

```java
public void put​(
String
key,

Object
value)
```

Sets the specified value with the specified key in the

ENGINE_SCOPE

Bindings

of the protected

context

field.

**Specified by:** put

in interface

ScriptEngine
**Parameters:** key

- The specified key.
**Parameters:** value

- The specified value.
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

---

#### put

public void put​(

String

key,

Object

value)

Sets the specified value with the specified key in the

ENGINE_SCOPE

Bindings

of the protected

context

field.

get

```java
public
Object
get​(
String
key)
```

Gets the value for the specified key in the

ENGINE_SCOPE

of the
protected

context

field.

**Specified by:** get

in interface

ScriptEngine
**Parameters:** key

- The key whose value is to be returned
**Returns:** The value for the specified key.
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

---

#### get

public

Object

get​(

String

key)

Gets the value for the specified key in the

ENGINE_SCOPE

of the
protected

context

field.

eval

```java
public
Object
eval​(
Reader
reader,

Bindings
bindings)
throws
ScriptException
```

eval(Reader, Bindings)

calls the abstract

eval(Reader, ScriptContext)

method, passing it a

ScriptContext

whose Reader, Writers and Bindings for scopes other that

ENGINE_SCOPE

are identical to those members of the protected

context

field. The specified

Bindings

is used instead of the

ENGINE_SCOPE

Bindings

of the

context

field.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** reader

- A

Reader

containing the source of the script.
**Parameters:** bindings

- A

Bindings

to use for the

ENGINE_SCOPE

while the script executes.
**Returns:** The return value from

eval(Reader, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

---

#### eval

public

Object

eval​(

Reader

reader,

Bindings

bindings)
throws

ScriptException

eval(Reader, Bindings)

calls the abstract

eval(Reader, ScriptContext)

method, passing it a

ScriptContext

whose Reader, Writers and Bindings for scopes other that

ENGINE_SCOPE

are identical to those members of the protected

context

field. The specified

Bindings

is used instead of the

ENGINE_SCOPE

Bindings

of the

context

field.

eval

```java
public
Object
eval​(
String
script,

Bindings
bindings)
throws
ScriptException
```

Same as

eval(Reader, Bindings)

except that the abstract

eval(String, ScriptContext)

is used.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** script

- A

String

containing the source of the script.
**Parameters:** bindings

- A

Bindings

to use as the

ENGINE_SCOPE

while the script executes.
**Returns:** The return value from

eval(String, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

---

#### eval

public

Object

eval​(

String

script,

Bindings

bindings)
throws

ScriptException

Same as

eval(Reader, Bindings)

except that the abstract

eval(String, ScriptContext)

is used.

eval

```java
public
Object
eval​(
Reader
reader)
throws
ScriptException
```

eval(Reader)

calls the abstract

eval(Reader, ScriptContext)

passing the value of the

context

field.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** reader

- A

Reader

containing the source of the script.
**Returns:** The return value from

eval(Reader, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

---

#### eval

public

Object

eval​(

Reader

reader)
throws

ScriptException

eval(Reader)

calls the abstract

eval(Reader, ScriptContext)

passing the value of the

context

field.

eval

```java
public
Object
eval​(
String
script)
throws
ScriptException
```

Same as

eval(Reader)

except that the abstract

eval(String, ScriptContext)

is used.

**Specified by:** eval

in interface

ScriptEngine
**Parameters:** script

- A

String

containing the source of the script.
**Returns:** The return value from

eval(String, ScriptContext)
**Throws:** ScriptException

- if an error occurs in script.
**Throws:** NullPointerException

- if any of the parameters is null.

---

#### eval

public

Object

eval​(

String

script)
throws

ScriptException

Same as

eval(Reader)

except that the abstract

eval(String, ScriptContext)

is used.

getScriptContext

```java
protected
ScriptContext
getScriptContext​(
Bindings
nn)
```

Returns a

SimpleScriptContext

. The

SimpleScriptContext

:

- Uses the specified

Bindings

for its

ENGINE_SCOPE
- Uses the

Bindings

returned by the abstract

getGlobalScope

method as its

GLOBAL_SCOPE
- Uses the Reader and Writer in the default

ScriptContext

of this

ScriptEngine

A

SimpleScriptContext

returned by this method is used to implement eval methods
using the abstract

eval(Reader,Bindings)

and

eval(String,Bindings)

versions.

**Parameters:** nn

- Bindings to use for the

ENGINE_SCOPE
**Returns:** The

SimpleScriptContext

---

#### getScriptContext

protected

ScriptContext

getScriptContext​(

Bindings

nn)

Returns a

SimpleScriptContext

. The

SimpleScriptContext

:

- Uses the specified

Bindings

for its

ENGINE_SCOPE
- Uses the

Bindings

returned by the abstract

getGlobalScope

method as its

GLOBAL_SCOPE
- Uses the Reader and Writer in the default

ScriptContext

of this

ScriptEngine

A

SimpleScriptContext

returned by this method is used to implement eval methods
using the abstract

eval(Reader,Bindings)

and

eval(String,Bindings)

versions.

Uses the specified

Bindings

for its

ENGINE_SCOPE

Uses the

Bindings

returned by the abstract

getGlobalScope

method as its

GLOBAL_SCOPE

Uses the Reader and Writer in the default

ScriptContext

of this

ScriptEngine

---

