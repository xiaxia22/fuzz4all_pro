# Class CompiledScript

**Source:** `java.scripting\javax\script\CompiledScript.html`

### Class Description

```java
public abstract class
CompiledScript

extends
Object
```

Extended by classes that store results of compilations. State
might be stored in the form of Java classes, Java class files or scripting
language opcodes. The script may be executed repeatedly
without reparsing.

Each

CompiledScript

is associated with a

ScriptEngine

-- A call to an

eval

method of the

CompiledScript

causes the execution of the script by the

ScriptEngine

. Changes in the state of the

ScriptEngine

caused by execution
of the

CompiledScript

may visible during subsequent executions of scripts by the engine.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public CompiledScript()

*No description found.*

---

### Method Details

#### public abstract
Object
eval​(
ScriptContext
context)
throws
ScriptException

Executes the program stored in this

CompiledScript

object.

**Parameters:**
- context

- A

ScriptContext

that is used in the same way as
the

ScriptContext

passed to the

eval

methods of

ScriptEngine

.

**Returns:**
- The value returned by the script execution, if any. Should return

null

if no value is returned by the script execution.

**Throws:**
- ScriptException

- if an error occurs.
- NullPointerException

- if context is null.

---

#### public
Object
eval​(
Bindings
bindings)
throws
ScriptException

Executes the program stored in the

CompiledScript

object using
the supplied

Bindings

of attributes as the

ENGINE_SCOPE

of the
associated

ScriptEngine

during script execution. If bindings is null,
then the effect of calling this method is same as that of eval(getEngine().getContext()).

.
The

GLOBAL_SCOPE

Bindings

,

Reader

and

Writer

associated with the default

ScriptContext

of the associated

ScriptEngine

are used.

**Parameters:**
- bindings

- The bindings of attributes used for the

ENGINE_SCOPE

.

**Returns:**
- The return value from the script execution

**Throws:**
- ScriptException

- if an error occurs.

---

#### public
Object
eval()
throws
ScriptException

Executes the program stored in the

CompiledScript

object. The
default

ScriptContext

of the associated

ScriptEngine

is used.
The effect of calling this method is same as that of eval(getEngine().getContext()).

**Returns:**
- The return value from the script execution

**Throws:**
- ScriptException

- if an error occurs.

---

#### public abstract
ScriptEngine
getEngine()

Returns the

ScriptEngine

whose

compile

method created this

CompiledScript

.
The

CompiledScript

will execute in this engine.

**Returns:**
- The

ScriptEngine

that created this

CompiledScript

---

### Additional Sections

#### Class CompiledScript

java.lang.Object

- javax.script.CompiledScript

javax.script.CompiledScript

```java
public abstract class
CompiledScript

extends
Object
```

Extended by classes that store results of compilations. State
might be stored in the form of Java classes, Java class files or scripting
language opcodes. The script may be executed repeatedly
without reparsing.

Each

CompiledScript

is associated with a

ScriptEngine

-- A call to an

eval

method of the

CompiledScript

causes the execution of the script by the

ScriptEngine

. Changes in the state of the

ScriptEngine

caused by execution
of the

CompiledScript

may visible during subsequent executions of scripts by the engine.

**Since:** 1.6

public abstract class

CompiledScript

extends

Object

Extended by classes that store results of compilations. State
might be stored in the form of Java classes, Java class files or scripting
language opcodes. The script may be executed repeatedly
without reparsing.

Each

CompiledScript

is associated with a

ScriptEngine

-- A call to an

eval

method of the

CompiledScript

causes the execution of the script by the

ScriptEngine

. Changes in the state of the

ScriptEngine

caused by execution
of the

CompiledScript

may visible during subsequent executions of scripts by the engine.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CompiledScript

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

eval

()

Executes the program stored in the

CompiledScript

object.

Object

eval

​(

Bindings

bindings)

Executes the program stored in the

CompiledScript

object using
the supplied

Bindings

of attributes as the

ENGINE_SCOPE

of the
associated

ScriptEngine

during script execution.

abstract

Object

eval

​(

ScriptContext

context)

Executes the program stored in this

CompiledScript

object.

abstract

ScriptEngine

getEngine

()

Returns the

ScriptEngine

whose

compile

method created this

CompiledScript

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

Constructor Summary

Constructors

Constructor

Description

CompiledScript

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

eval

()

Executes the program stored in the

CompiledScript

object.

Object

eval

​(

Bindings

bindings)

Executes the program stored in the

CompiledScript

object using
the supplied

Bindings

of attributes as the

ENGINE_SCOPE

of the
associated

ScriptEngine

during script execution.

abstract

Object

eval

​(

ScriptContext

context)

Executes the program stored in this

CompiledScript

object.

abstract

ScriptEngine

getEngine

()

Returns the

ScriptEngine

whose

compile

method created this

CompiledScript

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

---

#### Method Summary

Executes the program stored in the

CompiledScript

object.

Executes the program stored in the

CompiledScript

object using
the supplied

Bindings

of attributes as the

ENGINE_SCOPE

of the
associated

ScriptEngine

during script execution.

Executes the program stored in this

CompiledScript

object.

Returns the

ScriptEngine

whose

compile

method created this

CompiledScript

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CompiledScript

```java
public CompiledScript()
```

============ METHOD DETAIL ==========

- Method Detail

- eval

```java
public abstract
Object
eval​(
ScriptContext
context)
throws
ScriptException
```

Executes the program stored in this

CompiledScript

object.

**Parameters:** context

- A

ScriptContext

that is used in the same way as
the

ScriptContext

passed to the

eval

methods of

ScriptEngine

.
**Returns:** The value returned by the script execution, if any. Should return

null

if no value is returned by the script execution.
**Throws:** ScriptException

- if an error occurs.
**Throws:** NullPointerException

- if context is null.

- eval

```java
public
Object
eval​(
Bindings
bindings)
throws
ScriptException
```

Executes the program stored in the

CompiledScript

object using
the supplied

Bindings

of attributes as the

ENGINE_SCOPE

of the
associated

ScriptEngine

during script execution. If bindings is null,
then the effect of calling this method is same as that of eval(getEngine().getContext()).

.
The

GLOBAL_SCOPE

Bindings

,

Reader

and

Writer

associated with the default

ScriptContext

of the associated

ScriptEngine

are used.

**Parameters:** bindings

- The bindings of attributes used for the

ENGINE_SCOPE

.
**Returns:** The return value from the script execution
**Throws:** ScriptException

- if an error occurs.

- eval

```java
public
Object
eval()
throws
ScriptException
```

Executes the program stored in the

CompiledScript

object. The
default

ScriptContext

of the associated

ScriptEngine

is used.
The effect of calling this method is same as that of eval(getEngine().getContext()).

**Returns:** The return value from the script execution
**Throws:** ScriptException

- if an error occurs.

- getEngine

```java
public abstract
ScriptEngine
getEngine()
```

Returns the

ScriptEngine

whose

compile

method created this

CompiledScript

.
The

CompiledScript

will execute in this engine.

**Returns:** The

ScriptEngine

that created this

CompiledScript

Constructor Detail

- CompiledScript

```java
public CompiledScript()
```

---

#### Constructor Detail

CompiledScript

```java
public CompiledScript()
```

---

#### CompiledScript

public CompiledScript()

Method Detail

- eval

```java
public abstract
Object
eval​(
ScriptContext
context)
throws
ScriptException
```

Executes the program stored in this

CompiledScript

object.

**Parameters:** context

- A

ScriptContext

that is used in the same way as
the

ScriptContext

passed to the

eval

methods of

ScriptEngine

.
**Returns:** The value returned by the script execution, if any. Should return

null

if no value is returned by the script execution.
**Throws:** ScriptException

- if an error occurs.
**Throws:** NullPointerException

- if context is null.

- eval

```java
public
Object
eval​(
Bindings
bindings)
throws
ScriptException
```

Executes the program stored in the

CompiledScript

object using
the supplied

Bindings

of attributes as the

ENGINE_SCOPE

of the
associated

ScriptEngine

during script execution. If bindings is null,
then the effect of calling this method is same as that of eval(getEngine().getContext()).

.
The

GLOBAL_SCOPE

Bindings

,

Reader

and

Writer

associated with the default

ScriptContext

of the associated

ScriptEngine

are used.

**Parameters:** bindings

- The bindings of attributes used for the

ENGINE_SCOPE

.
**Returns:** The return value from the script execution
**Throws:** ScriptException

- if an error occurs.

- eval

```java
public
Object
eval()
throws
ScriptException
```

Executes the program stored in the

CompiledScript

object. The
default

ScriptContext

of the associated

ScriptEngine

is used.
The effect of calling this method is same as that of eval(getEngine().getContext()).

**Returns:** The return value from the script execution
**Throws:** ScriptException

- if an error occurs.

- getEngine

```java
public abstract
ScriptEngine
getEngine()
```

Returns the

ScriptEngine

whose

compile

method created this

CompiledScript

.
The

CompiledScript

will execute in this engine.

**Returns:** The

ScriptEngine

that created this

CompiledScript

---

#### Method Detail

eval

```java
public abstract
Object
eval​(
ScriptContext
context)
throws
ScriptException
```

Executes the program stored in this

CompiledScript

object.

**Parameters:** context

- A

ScriptContext

that is used in the same way as
the

ScriptContext

passed to the

eval

methods of

ScriptEngine

.
**Returns:** The value returned by the script execution, if any. Should return

null

if no value is returned by the script execution.
**Throws:** ScriptException

- if an error occurs.
**Throws:** NullPointerException

- if context is null.

---

#### eval

public abstract

Object

eval​(

ScriptContext

context)
throws

ScriptException

Executes the program stored in this

CompiledScript

object.

eval

```java
public
Object
eval​(
Bindings
bindings)
throws
ScriptException
```

Executes the program stored in the

CompiledScript

object using
the supplied

Bindings

of attributes as the

ENGINE_SCOPE

of the
associated

ScriptEngine

during script execution. If bindings is null,
then the effect of calling this method is same as that of eval(getEngine().getContext()).

.
The

GLOBAL_SCOPE

Bindings

,

Reader

and

Writer

associated with the default

ScriptContext

of the associated

ScriptEngine

are used.

**Parameters:** bindings

- The bindings of attributes used for the

ENGINE_SCOPE

.
**Returns:** The return value from the script execution
**Throws:** ScriptException

- if an error occurs.

---

#### eval

public

Object

eval​(

Bindings

bindings)
throws

ScriptException

Executes the program stored in the

CompiledScript

object using
the supplied

Bindings

of attributes as the

ENGINE_SCOPE

of the
associated

ScriptEngine

during script execution. If bindings is null,
then the effect of calling this method is same as that of eval(getEngine().getContext()).

.
The

GLOBAL_SCOPE

Bindings

,

Reader

and

Writer

associated with the default

ScriptContext

of the associated

ScriptEngine

are used.

.
The

GLOBAL_SCOPE

Bindings

,

Reader

and

Writer

associated with the default

ScriptContext

of the associated

ScriptEngine

are used.

eval

```java
public
Object
eval()
throws
ScriptException
```

Executes the program stored in the

CompiledScript

object. The
default

ScriptContext

of the associated

ScriptEngine

is used.
The effect of calling this method is same as that of eval(getEngine().getContext()).

**Returns:** The return value from the script execution
**Throws:** ScriptException

- if an error occurs.

---

#### eval

public

Object

eval()
throws

ScriptException

Executes the program stored in the

CompiledScript

object. The
default

ScriptContext

of the associated

ScriptEngine

is used.
The effect of calling this method is same as that of eval(getEngine().getContext()).

getEngine

```java
public abstract
ScriptEngine
getEngine()
```

Returns the

ScriptEngine

whose

compile

method created this

CompiledScript

.
The

CompiledScript

will execute in this engine.

**Returns:** The

ScriptEngine

that created this

CompiledScript

---

#### getEngine

public abstract

ScriptEngine

getEngine()

Returns the

ScriptEngine

whose

compile

method created this

CompiledScript

.
The

CompiledScript

will execute in this engine.

---

