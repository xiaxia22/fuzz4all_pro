# Interface Compilable

**Source:** `java.scripting\javax\script\Compilable.html`

### Class Description

```java
public interface
Compilable
```

The optional interface implemented by ScriptEngines whose methods compile scripts
to a form that can be executed repeatedly without recompilation.

**All Known Implementing Classes:** NashornScriptEngine

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CompiledScript
compile​(
String
script)
throws
ScriptException

Compiles the script (source represented as a

String

) for
later execution.

**Parameters:**
- script

- The source of the script, represented as a

String

.

**Returns:**
- An instance of a subclass of

CompiledScript

to be executed later using one
of the

eval

methods of

CompiledScript

.

**Throws:**
- ScriptException

- if compilation fails.
- NullPointerException

- if the argument is null.

---

#### CompiledScript
compile​(
Reader
script)
throws
ScriptException

Compiles the script (source read from

Reader

) for
later execution. Functionality is identical to

compile(String)

other than the way in which the source is
passed.

**Parameters:**
- script

- The reader from which the script source is obtained.

**Returns:**
- An instance of a subclass of

CompiledScript

to be executed
later using one of its

eval

methods of

CompiledScript

.

**Throws:**
- ScriptException

- if compilation fails.
- NullPointerException

- if argument is null.

---

### Additional Sections

#### Interface Compilable

**All Known Implementing Classes:** NashornScriptEngine

```java
public interface
Compilable
```

The optional interface implemented by ScriptEngines whose methods compile scripts
to a form that can be executed repeatedly without recompilation.

**Since:** 1.6

public interface

Compilable

The optional interface implemented by ScriptEngines whose methods compile scripts
to a form that can be executed repeatedly without recompilation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CompiledScript

compile

​(

Reader

script)

Compiles the script (source read from

Reader

) for
later execution.

CompiledScript

compile

​(

String

script)

Compiles the script (source represented as a

String

) for
later execution.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CompiledScript

compile

​(

Reader

script)

Compiles the script (source read from

Reader

) for
later execution.

CompiledScript

compile

​(

String

script)

Compiles the script (source represented as a

String

) for
later execution.

---

#### Method Summary

Compiles the script (source read from

Reader

) for
later execution.

Compiles the script (source represented as a

String

) for
later execution.

============ METHOD DETAIL ==========

- Method Detail

- compile

```java
CompiledScript
compile​(
String
script)
throws
ScriptException
```

Compiles the script (source represented as a

String

) for
later execution.

**Parameters:** script

- The source of the script, represented as a

String

.
**Returns:** An instance of a subclass of

CompiledScript

to be executed later using one
of the

eval

methods of

CompiledScript

.
**Throws:** ScriptException

- if compilation fails.
**Throws:** NullPointerException

- if the argument is null.

- compile

```java
CompiledScript
compile​(
Reader
script)
throws
ScriptException
```

Compiles the script (source read from

Reader

) for
later execution. Functionality is identical to

compile(String)

other than the way in which the source is
passed.

**Parameters:** script

- The reader from which the script source is obtained.
**Returns:** An instance of a subclass of

CompiledScript

to be executed
later using one of its

eval

methods of

CompiledScript

.
**Throws:** ScriptException

- if compilation fails.
**Throws:** NullPointerException

- if argument is null.

Method Detail

- compile

```java
CompiledScript
compile​(
String
script)
throws
ScriptException
```

Compiles the script (source represented as a

String

) for
later execution.

**Parameters:** script

- The source of the script, represented as a

String

.
**Returns:** An instance of a subclass of

CompiledScript

to be executed later using one
of the

eval

methods of

CompiledScript

.
**Throws:** ScriptException

- if compilation fails.
**Throws:** NullPointerException

- if the argument is null.

- compile

```java
CompiledScript
compile​(
Reader
script)
throws
ScriptException
```

Compiles the script (source read from

Reader

) for
later execution. Functionality is identical to

compile(String)

other than the way in which the source is
passed.

**Parameters:** script

- The reader from which the script source is obtained.
**Returns:** An instance of a subclass of

CompiledScript

to be executed
later using one of its

eval

methods of

CompiledScript

.
**Throws:** ScriptException

- if compilation fails.
**Throws:** NullPointerException

- if argument is null.

---

#### Method Detail

compile

```java
CompiledScript
compile​(
String
script)
throws
ScriptException
```

Compiles the script (source represented as a

String

) for
later execution.

**Parameters:** script

- The source of the script, represented as a

String

.
**Returns:** An instance of a subclass of

CompiledScript

to be executed later using one
of the

eval

methods of

CompiledScript

.
**Throws:** ScriptException

- if compilation fails.
**Throws:** NullPointerException

- if the argument is null.

---

#### compile

CompiledScript

compile​(

String

script)
throws

ScriptException

Compiles the script (source represented as a

String

) for
later execution.

compile

```java
CompiledScript
compile​(
Reader
script)
throws
ScriptException
```

Compiles the script (source read from

Reader

) for
later execution. Functionality is identical to

compile(String)

other than the way in which the source is
passed.

**Parameters:** script

- The reader from which the script source is obtained.
**Returns:** An instance of a subclass of

CompiledScript

to be executed
later using one of its

eval

methods of

CompiledScript

.
**Throws:** ScriptException

- if compilation fails.
**Throws:** NullPointerException

- if argument is null.

---

#### compile

CompiledScript

compile​(

Reader

script)
throws

ScriptException

Compiles the script (source read from

Reader

) for
later execution. Functionality is identical to

compile(String)

other than the way in which the source is
passed.

---

