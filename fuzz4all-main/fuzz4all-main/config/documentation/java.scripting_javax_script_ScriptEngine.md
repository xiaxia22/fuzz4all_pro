# Interface ScriptEngine

**Source:** `java.scripting\javax\script\ScriptEngine.html`

### Class Description

```java
public interface
ScriptEngine
```

ScriptEngine

is the fundamental interface whose methods must be
fully functional in every implementation of this specification.

These methods provide basic scripting functionality. Applications written to this
simple interface are expected to work with minimal modifications in every implementation.
It includes methods that execute scripts, and ones that set and get values.

The values are key/value pairs of two types. The first type of pairs consists of
those whose keys are reserved and defined in this specification or by individual
implementations. The values in the pairs with reserved keys have specified meanings.

The other type of pairs consists of those that create Java language Bindings, the values are
usually represented in scripts by the corresponding keys or by decorated forms of them.

**All Known Implementing Classes:** AbstractScriptEngine

,

NashornScriptEngine

---

### Field Details

#### static final
String
ARGV

Reserved key for a named value that passes
an array of positional arguments to a script.

**See Also:**
- Constant Field Values

---

#### static final
String
FILENAME

Reserved key for a named value that is
the name of the file being executed.

**See Also:**
- Constant Field Values

---

#### static final
String
ENGINE

Reserved key for a named value that is
the name of the

ScriptEngine

implementation.

**See Also:**
- Constant Field Values

---

#### static final
String
ENGINE_VERSION

Reserved key for a named value that identifies
the version of the

ScriptEngine

implementation.

**See Also:**
- Constant Field Values

---

#### static final
String
NAME

Reserved key for a named value that identifies
the short name of the scripting language. The name is used by the

ScriptEngineManager

to locate a

ScriptEngine

with a given name in the

getEngineByName

method.

**See Also:**
- Constant Field Values

---

#### static final
String
LANGUAGE

Reserved key for a named value that is
the full name of Scripting Language supported by the implementation.

**See Also:**
- Constant Field Values

---

#### static final
String
LANGUAGE_VERSION

Reserved key for the named value that identifies
the version of the scripting language supported by the implementation.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Object
eval​(
String
script,

ScriptContext
context)
throws
ScriptException

Causes the immediate execution of the script whose source is the String
passed as the first argument. The script may be reparsed or recompiled before
execution. State left in the engine from previous executions, including
variable values and compiled procedures may be visible during this execution.

**Parameters:**
- script

- The script to be executed by the script engine.
- context

- A

ScriptContext

exposing sets of attributes in
different scopes. The meanings of the scopes

ScriptContext.GLOBAL_SCOPE

,
and

ScriptContext.ENGINE_SCOPE

are defined in the specification.

The

ENGINE_SCOPE

Bindings

of the

ScriptContext

contains the
bindings of scripting variables to application objects to be used during this
script execution.

**Returns:**
- The value returned from the execution of the script.

**Throws:**
- ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
- NullPointerException

- if either argument is null.

---

#### Object
eval​(
Reader
reader,

ScriptContext
context)
throws
ScriptException

Same as

eval(String, ScriptContext)

where the source of the script
is read from a

Reader

.

**Parameters:**
- reader

- The source of the script to be executed by the script engine.
- context

- The

ScriptContext

passed to the script engine.

**Returns:**
- The value returned from the execution of the script.

**Throws:**
- ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
- NullPointerException

- if either argument is null.

---

#### Object
eval​(
String
script)
throws
ScriptException

Executes the specified script. The default

ScriptContext

for the

ScriptEngine

is used.

**Parameters:**
- script

- The script language source to be executed.

**Returns:**
- The value returned from the execution of the script.

**Throws:**
- ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
- NullPointerException

- if the argument is null.

---

#### Object
eval​(
Reader
reader)
throws
ScriptException

Same as

eval(String)

except that the source of the script is
provided as a

Reader

**Parameters:**
- reader

- The source of the script.

**Returns:**
- The value returned by the script.

**Throws:**
- ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
- NullPointerException

- if the argument is null.

---

#### Object
eval​(
String
script,

Bindings
n)
throws
ScriptException

Executes the script using the

Bindings

argument as the

ENGINE_SCOPE

Bindings

of the

ScriptEngine

during the script execution. The

Reader

,

Writer

and non-

ENGINE_SCOPE

Bindings

of the
default

ScriptContext

are used. The

ENGINE_SCOPE

Bindings

of the

ScriptEngine

is not changed, and its
mappings are unaltered by the script execution.

**Parameters:**
- script

- The source for the script.
- n

- The

Bindings

of attributes to be used for script execution.

**Returns:**
- The value returned by the script.

**Throws:**
- ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
- NullPointerException

- if either argument is null.

---

#### Object
eval​(
Reader
reader,

Bindings
n)
throws
ScriptException

Same as

eval(String, Bindings)

except that the source of the script
is provided as a

Reader

.

**Parameters:**
- reader

- The source of the script.
- n

- The

Bindings

of attributes.

**Returns:**
- The value returned by the script.

**Throws:**
- ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
- NullPointerException

- if either argument is null.

---

#### void put​(
String
key,

Object
value)

Sets a key/value pair in the state of the ScriptEngine that may either create
a Java Language Binding to be used in the execution of scripts or be used in some
other way, depending on whether the key is reserved. Must have the same effect as

getBindings(ScriptContext.ENGINE_SCOPE).put

.

**Parameters:**
- key

- The name of named value to add
- value

- The value of named value to add.

**Throws:**
- NullPointerException

- if key is null.
- IllegalArgumentException

- if key is empty.

---

#### Object
get​(
String
key)

Retrieves a value set in the state of this engine. The value might be one
which was set using

setValue

or some other value in the state
of the

ScriptEngine

, depending on the implementation. Must have the same effect
as

getBindings(ScriptContext.ENGINE_SCOPE).get

**Parameters:**
- key

- The key whose value is to be returned

**Returns:**
- the value for the given key

**Throws:**
- NullPointerException

- if key is null.
- IllegalArgumentException

- if key is empty.

---

#### Bindings
getBindings​(int scope)

Returns a scope of named values. The possible scopes are:

- ScriptContext.GLOBAL_SCOPE

- The set of named values representing global
scope. If this

ScriptEngine

is created by a

ScriptEngineManager

,
then the manager sets global scope bindings. This may be

null

if no global
scope is associated with this

ScriptEngine
- ScriptContext.ENGINE_SCOPE

- The set of named values representing the state of
this

ScriptEngine

. The values are generally visible in scripts using
the associated keys as variable names.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The

Bindings

instances that are returned must be identical to those returned by the

getBindings

method of

ScriptContext

called with corresponding arguments on
the default

ScriptContext

of the

ScriptEngine

.

**Parameters:**
- scope

- Either

ScriptContext.ENGINE_SCOPE

or

ScriptContext.GLOBAL_SCOPE

which specifies the

Bindings

to return. Implementations of

ScriptContext

may define additional scopes. If the default

ScriptContext

of the

ScriptEngine

defines additional scopes, any of them can be passed to get the corresponding

Bindings

.

**Returns:**
- The

Bindings

with the specified scope.

**Throws:**
- IllegalArgumentException

- if specified scope is invalid

---

#### void setBindings​(
Bindings
bindings,
int scope)

Sets a scope of named values to be used by scripts. The possible scopes are:

- ScriptContext.ENGINE_SCOPE

- The specified

Bindings

replaces the
engine scope of the

ScriptEngine

.
- ScriptContext.GLOBAL_SCOPE

- The specified

Bindings

must be visible
as the

GLOBAL_SCOPE

.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The method must have the same effect as calling the

setBindings

method of

ScriptContext

with the corresponding value of

scope

on the default

ScriptContext

of the

ScriptEngine

.

**Parameters:**
- bindings

- The

Bindings

for the specified scope.
- scope

- The specified scope. Either

ScriptContext.ENGINE_SCOPE

,

ScriptContext.GLOBAL_SCOPE

, or any other valid value of scope.

**Throws:**
- IllegalArgumentException

- if the scope is invalid
- NullPointerException

- if the bindings is null and the scope is

ScriptContext.ENGINE_SCOPE

---

#### Bindings
createBindings()

Returns an uninitialized

Bindings

.

**Returns:**
- A

Bindings

that can be used to replace the state of this

ScriptEngine

.

---

#### ScriptContext
getContext()

Returns the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

**Returns:**
- The default

ScriptContext

of the

ScriptEngine

.

---

#### void setContext​(
ScriptContext
context)

Sets the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

**Parameters:**
- context

- A

ScriptContext

that will replace the default

ScriptContext

in
the

ScriptEngine

.

**Throws:**
- NullPointerException

- if context is null.

---

#### ScriptEngineFactory
getFactory()

Returns a

ScriptEngineFactory

for the class to which this

ScriptEngine

belongs.

**Returns:**
- The

ScriptEngineFactory

---

### Additional Sections

#### Interface ScriptEngine

**All Known Implementing Classes:** AbstractScriptEngine

,

NashornScriptEngine

```java
public interface
ScriptEngine
```

ScriptEngine

is the fundamental interface whose methods must be
fully functional in every implementation of this specification.

These methods provide basic scripting functionality. Applications written to this
simple interface are expected to work with minimal modifications in every implementation.
It includes methods that execute scripts, and ones that set and get values.

The values are key/value pairs of two types. The first type of pairs consists of
those whose keys are reserved and defined in this specification or by individual
implementations. The values in the pairs with reserved keys have specified meanings.

The other type of pairs consists of those that create Java language Bindings, the values are
usually represented in scripts by the corresponding keys or by decorated forms of them.

**Since:** 1.6

public interface

ScriptEngine

ScriptEngine

is the fundamental interface whose methods must be
fully functional in every implementation of this specification.

These methods provide basic scripting functionality. Applications written to this
simple interface are expected to work with minimal modifications in every implementation.
It includes methods that execute scripts, and ones that set and get values.

The values are key/value pairs of two types. The first type of pairs consists of
those whose keys are reserved and defined in this specification or by individual
implementations. The values in the pairs with reserved keys have specified meanings.

The other type of pairs consists of those that create Java language Bindings, the values are
usually represented in scripts by the corresponding keys or by decorated forms of them.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

ARGV

Reserved key for a named value that passes
an array of positional arguments to a script.

static

String

ENGINE

Reserved key for a named value that is
the name of the

ScriptEngine

implementation.

static

String

ENGINE_VERSION

Reserved key for a named value that identifies
the version of the

ScriptEngine

implementation.

static

String

FILENAME

Reserved key for a named value that is
the name of the file being executed.

static

String

LANGUAGE

Reserved key for a named value that is
the full name of Scripting Language supported by the implementation.

static

String

LANGUAGE_VERSION

Reserved key for the named value that identifies
the version of the scripting language supported by the implementation.

static

String

NAME

Reserved key for a named value that identifies
the short name of the scripting language.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Bindings

createBindings

()

Returns an uninitialized

Bindings

.

Object

eval

​(

Reader

reader)

Same as

eval(String)

except that the source of the script is
provided as a

Reader

Object

eval

​(

Reader

reader,

Bindings

n)

Same as

eval(String, Bindings)

except that the source of the script
is provided as a

Reader

.

Object

eval

​(

Reader

reader,

ScriptContext

context)

Same as

eval(String, ScriptContext)

where the source of the script
is read from a

Reader

.

Object

eval

​(

String

script)

Executes the specified script.

Object

eval

​(

String

script,

Bindings

n)

Executes the script using the

Bindings

argument as the

ENGINE_SCOPE

Bindings

of the

ScriptEngine

during the script execution.

Object

eval

​(

String

script,

ScriptContext

context)

Causes the immediate execution of the script whose source is the String
passed as the first argument.

Object

get

​(

String

key)

Retrieves a value set in the state of this engine.

Bindings

getBindings

​(int scope)

Returns a scope of named values.

ScriptContext

getContext

()

Returns the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

ScriptEngineFactory

getFactory

()

Returns a

ScriptEngineFactory

for the class to which this

ScriptEngine

belongs.

void

put

​(

String

key,

Object

value)

Sets a key/value pair in the state of the ScriptEngine that may either create
a Java Language Binding to be used in the execution of scripts or be used in some
other way, depending on whether the key is reserved.

void

setBindings

​(

Bindings

bindings,
int scope)

Sets a scope of named values to be used by scripts.

void

setContext

​(

ScriptContext

context)

Sets the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

ARGV

Reserved key for a named value that passes
an array of positional arguments to a script.

static

String

ENGINE

Reserved key for a named value that is
the name of the

ScriptEngine

implementation.

static

String

ENGINE_VERSION

Reserved key for a named value that identifies
the version of the

ScriptEngine

implementation.

static

String

FILENAME

Reserved key for a named value that is
the name of the file being executed.

static

String

LANGUAGE

Reserved key for a named value that is
the full name of Scripting Language supported by the implementation.

static

String

LANGUAGE_VERSION

Reserved key for the named value that identifies
the version of the scripting language supported by the implementation.

static

String

NAME

Reserved key for a named value that identifies
the short name of the scripting language.

---

#### Field Summary

Reserved key for a named value that passes
an array of positional arguments to a script.

Reserved key for a named value that is
the name of the

ScriptEngine

implementation.

Reserved key for a named value that identifies
the version of the

ScriptEngine

implementation.

Reserved key for a named value that is
the name of the file being executed.

Reserved key for a named value that is
the full name of Scripting Language supported by the implementation.

Reserved key for the named value that identifies
the version of the scripting language supported by the implementation.

Reserved key for a named value that identifies
the short name of the scripting language.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Bindings

createBindings

()

Returns an uninitialized

Bindings

.

Object

eval

​(

Reader

reader)

Same as

eval(String)

except that the source of the script is
provided as a

Reader

Object

eval

​(

Reader

reader,

Bindings

n)

Same as

eval(String, Bindings)

except that the source of the script
is provided as a

Reader

.

Object

eval

​(

Reader

reader,

ScriptContext

context)

Same as

eval(String, ScriptContext)

where the source of the script
is read from a

Reader

.

Object

eval

​(

String

script)

Executes the specified script.

Object

eval

​(

String

script,

Bindings

n)

Executes the script using the

Bindings

argument as the

ENGINE_SCOPE

Bindings

of the

ScriptEngine

during the script execution.

Object

eval

​(

String

script,

ScriptContext

context)

Causes the immediate execution of the script whose source is the String
passed as the first argument.

Object

get

​(

String

key)

Retrieves a value set in the state of this engine.

Bindings

getBindings

​(int scope)

Returns a scope of named values.

ScriptContext

getContext

()

Returns the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

ScriptEngineFactory

getFactory

()

Returns a

ScriptEngineFactory

for the class to which this

ScriptEngine

belongs.

void

put

​(

String

key,

Object

value)

Sets a key/value pair in the state of the ScriptEngine that may either create
a Java Language Binding to be used in the execution of scripts or be used in some
other way, depending on whether the key is reserved.

void

setBindings

​(

Bindings

bindings,
int scope)

Sets a scope of named values to be used by scripts.

void

setContext

​(

ScriptContext

context)

Sets the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

---

#### Method Summary

Returns an uninitialized

Bindings

.

Same as

eval(String)

except that the source of the script is
provided as a

Reader

Same as

eval(String, Bindings)

except that the source of the script
is provided as a

Reader

.

Same as

eval(String, ScriptContext)

where the source of the script
is read from a

Reader

.

Executes the specified script.

Executes the script using the

Bindings

argument as the

ENGINE_SCOPE

Bindings

of the

ScriptEngine

during the script execution.

Causes the immediate execution of the script whose source is the String
passed as the first argument.

Retrieves a value set in the state of this engine.

Returns a scope of named values.

Returns the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

Returns a

ScriptEngineFactory

for the class to which this

ScriptEngine

belongs.

Sets a key/value pair in the state of the ScriptEngine that may either create
a Java Language Binding to be used in the execution of scripts or be used in some
other way, depending on whether the key is reserved.

Sets a scope of named values to be used by scripts.

Sets the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

============ FIELD DETAIL ===========

- Field Detail

- ARGV

```java
static final
String
ARGV
```

Reserved key for a named value that passes
an array of positional arguments to a script.

**See Also:** Constant Field Values

- FILENAME

```java
static final
String
FILENAME
```

Reserved key for a named value that is
the name of the file being executed.

**See Also:** Constant Field Values

- ENGINE

```java
static final
String
ENGINE
```

Reserved key for a named value that is
the name of the

ScriptEngine

implementation.

**See Also:** Constant Field Values

- ENGINE_VERSION

```java
static final
String
ENGINE_VERSION
```

Reserved key for a named value that identifies
the version of the

ScriptEngine

implementation.

**See Also:** Constant Field Values

- NAME

```java
static final
String
NAME
```

Reserved key for a named value that identifies
the short name of the scripting language. The name is used by the

ScriptEngineManager

to locate a

ScriptEngine

with a given name in the

getEngineByName

method.

**See Also:** Constant Field Values

- LANGUAGE

```java
static final
String
LANGUAGE
```

Reserved key for a named value that is
the full name of Scripting Language supported by the implementation.

**See Also:** Constant Field Values

- LANGUAGE_VERSION

```java
static final
String
LANGUAGE_VERSION
```

Reserved key for the named value that identifies
the version of the scripting language supported by the implementation.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- eval

```java
Object
eval​(
String
script,

ScriptContext
context)
throws
ScriptException
```

Causes the immediate execution of the script whose source is the String
passed as the first argument. The script may be reparsed or recompiled before
execution. State left in the engine from previous executions, including
variable values and compiled procedures may be visible during this execution.

**Parameters:** script

- The script to be executed by the script engine.
**Parameters:** context

- A

ScriptContext

exposing sets of attributes in
different scopes. The meanings of the scopes

ScriptContext.GLOBAL_SCOPE

,
and

ScriptContext.ENGINE_SCOPE

are defined in the specification.

The

ENGINE_SCOPE

Bindings

of the

ScriptContext

contains the
bindings of scripting variables to application objects to be used during this
script execution.
**Returns:** The value returned from the execution of the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

- eval

```java
Object
eval​(
Reader
reader,

ScriptContext
context)
throws
ScriptException
```

Same as

eval(String, ScriptContext)

where the source of the script
is read from a

Reader

.

**Parameters:** reader

- The source of the script to be executed by the script engine.
**Parameters:** context

- The

ScriptContext

passed to the script engine.
**Returns:** The value returned from the execution of the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

- eval

```java
Object
eval​(
String
script)
throws
ScriptException
```

Executes the specified script. The default

ScriptContext

for the

ScriptEngine

is used.

**Parameters:** script

- The script language source to be executed.
**Returns:** The value returned from the execution of the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if the argument is null.

- eval

```java
Object
eval​(
Reader
reader)
throws
ScriptException
```

Same as

eval(String)

except that the source of the script is
provided as a

Reader

**Parameters:** reader

- The source of the script.
**Returns:** The value returned by the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if the argument is null.

- eval

```java
Object
eval​(
String
script,

Bindings
n)
throws
ScriptException
```

Executes the script using the

Bindings

argument as the

ENGINE_SCOPE

Bindings

of the

ScriptEngine

during the script execution. The

Reader

,

Writer

and non-

ENGINE_SCOPE

Bindings

of the
default

ScriptContext

are used. The

ENGINE_SCOPE

Bindings

of the

ScriptEngine

is not changed, and its
mappings are unaltered by the script execution.

**Parameters:** script

- The source for the script.
**Parameters:** n

- The

Bindings

of attributes to be used for script execution.
**Returns:** The value returned by the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

- eval

```java
Object
eval​(
Reader
reader,

Bindings
n)
throws
ScriptException
```

Same as

eval(String, Bindings)

except that the source of the script
is provided as a

Reader

.

**Parameters:** reader

- The source of the script.
**Parameters:** n

- The

Bindings

of attributes.
**Returns:** The value returned by the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

- put

```java
void put​(
String
key,

Object
value)
```

Sets a key/value pair in the state of the ScriptEngine that may either create
a Java Language Binding to be used in the execution of scripts or be used in some
other way, depending on whether the key is reserved. Must have the same effect as

getBindings(ScriptContext.ENGINE_SCOPE).put

.

**Parameters:** key

- The name of named value to add
**Parameters:** value

- The value of named value to add.
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

- get

```java
Object
get​(
String
key)
```

Retrieves a value set in the state of this engine. The value might be one
which was set using

setValue

or some other value in the state
of the

ScriptEngine

, depending on the implementation. Must have the same effect
as

getBindings(ScriptContext.ENGINE_SCOPE).get

**Parameters:** key

- The key whose value is to be returned
**Returns:** the value for the given key
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

- getBindings

```java
Bindings
getBindings​(int scope)
```

Returns a scope of named values. The possible scopes are:

- ScriptContext.GLOBAL_SCOPE

- The set of named values representing global
scope. If this

ScriptEngine

is created by a

ScriptEngineManager

,
then the manager sets global scope bindings. This may be

null

if no global
scope is associated with this

ScriptEngine
- ScriptContext.ENGINE_SCOPE

- The set of named values representing the state of
this

ScriptEngine

. The values are generally visible in scripts using
the associated keys as variable names.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The

Bindings

instances that are returned must be identical to those returned by the

getBindings

method of

ScriptContext

called with corresponding arguments on
the default

ScriptContext

of the

ScriptEngine

.

**Parameters:** scope

- Either

ScriptContext.ENGINE_SCOPE

or

ScriptContext.GLOBAL_SCOPE

which specifies the

Bindings

to return. Implementations of

ScriptContext

may define additional scopes. If the default

ScriptContext

of the

ScriptEngine

defines additional scopes, any of them can be passed to get the corresponding

Bindings

.
**Returns:** The

Bindings

with the specified scope.
**Throws:** IllegalArgumentException

- if specified scope is invalid

- setBindings

```java
void setBindings​(
Bindings
bindings,
int scope)
```

Sets a scope of named values to be used by scripts. The possible scopes are:

- ScriptContext.ENGINE_SCOPE

- The specified

Bindings

replaces the
engine scope of the

ScriptEngine

.
- ScriptContext.GLOBAL_SCOPE

- The specified

Bindings

must be visible
as the

GLOBAL_SCOPE

.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The method must have the same effect as calling the

setBindings

method of

ScriptContext

with the corresponding value of

scope

on the default

ScriptContext

of the

ScriptEngine

.

**Parameters:** bindings

- The

Bindings

for the specified scope.
**Parameters:** scope

- The specified scope. Either

ScriptContext.ENGINE_SCOPE

,

ScriptContext.GLOBAL_SCOPE

, or any other valid value of scope.
**Throws:** IllegalArgumentException

- if the scope is invalid
**Throws:** NullPointerException

- if the bindings is null and the scope is

ScriptContext.ENGINE_SCOPE

- createBindings

```java
Bindings
createBindings()
```

Returns an uninitialized

Bindings

.

**Returns:** A

Bindings

that can be used to replace the state of this

ScriptEngine

.

- getContext

```java
ScriptContext
getContext()
```

Returns the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

**Returns:** The default

ScriptContext

of the

ScriptEngine

.

- setContext

```java
void setContext​(
ScriptContext
context)
```

Sets the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

**Parameters:** context

- A

ScriptContext

that will replace the default

ScriptContext

in
the

ScriptEngine

.
**Throws:** NullPointerException

- if context is null.

- getFactory

```java
ScriptEngineFactory
getFactory()
```

Returns a

ScriptEngineFactory

for the class to which this

ScriptEngine

belongs.

**Returns:** The

ScriptEngineFactory

Field Detail

- ARGV

```java
static final
String
ARGV
```

Reserved key for a named value that passes
an array of positional arguments to a script.

**See Also:** Constant Field Values

- FILENAME

```java
static final
String
FILENAME
```

Reserved key for a named value that is
the name of the file being executed.

**See Also:** Constant Field Values

- ENGINE

```java
static final
String
ENGINE
```

Reserved key for a named value that is
the name of the

ScriptEngine

implementation.

**See Also:** Constant Field Values

- ENGINE_VERSION

```java
static final
String
ENGINE_VERSION
```

Reserved key for a named value that identifies
the version of the

ScriptEngine

implementation.

**See Also:** Constant Field Values

- NAME

```java
static final
String
NAME
```

Reserved key for a named value that identifies
the short name of the scripting language. The name is used by the

ScriptEngineManager

to locate a

ScriptEngine

with a given name in the

getEngineByName

method.

**See Also:** Constant Field Values

- LANGUAGE

```java
static final
String
LANGUAGE
```

Reserved key for a named value that is
the full name of Scripting Language supported by the implementation.

**See Also:** Constant Field Values

- LANGUAGE_VERSION

```java
static final
String
LANGUAGE_VERSION
```

Reserved key for the named value that identifies
the version of the scripting language supported by the implementation.

**See Also:** Constant Field Values

---

#### Field Detail

ARGV

```java
static final
String
ARGV
```

Reserved key for a named value that passes
an array of positional arguments to a script.

**See Also:** Constant Field Values

---

#### ARGV

static final

String

ARGV

Reserved key for a named value that passes
an array of positional arguments to a script.

FILENAME

```java
static final
String
FILENAME
```

Reserved key for a named value that is
the name of the file being executed.

**See Also:** Constant Field Values

---

#### FILENAME

static final

String

FILENAME

Reserved key for a named value that is
the name of the file being executed.

ENGINE

```java
static final
String
ENGINE
```

Reserved key for a named value that is
the name of the

ScriptEngine

implementation.

**See Also:** Constant Field Values

---

#### ENGINE

static final

String

ENGINE

Reserved key for a named value that is
the name of the

ScriptEngine

implementation.

ENGINE_VERSION

```java
static final
String
ENGINE_VERSION
```

Reserved key for a named value that identifies
the version of the

ScriptEngine

implementation.

**See Also:** Constant Field Values

---

#### ENGINE_VERSION

static final

String

ENGINE_VERSION

Reserved key for a named value that identifies
the version of the

ScriptEngine

implementation.

NAME

```java
static final
String
NAME
```

Reserved key for a named value that identifies
the short name of the scripting language. The name is used by the

ScriptEngineManager

to locate a

ScriptEngine

with a given name in the

getEngineByName

method.

**See Also:** Constant Field Values

---

#### NAME

static final

String

NAME

Reserved key for a named value that identifies
the short name of the scripting language. The name is used by the

ScriptEngineManager

to locate a

ScriptEngine

with a given name in the

getEngineByName

method.

LANGUAGE

```java
static final
String
LANGUAGE
```

Reserved key for a named value that is
the full name of Scripting Language supported by the implementation.

**See Also:** Constant Field Values

---

#### LANGUAGE

static final

String

LANGUAGE

Reserved key for a named value that is
the full name of Scripting Language supported by the implementation.

LANGUAGE_VERSION

```java
static final
String
LANGUAGE_VERSION
```

Reserved key for the named value that identifies
the version of the scripting language supported by the implementation.

**See Also:** Constant Field Values

---

#### LANGUAGE_VERSION

static final

String

LANGUAGE_VERSION

Reserved key for the named value that identifies
the version of the scripting language supported by the implementation.

Method Detail

- eval

```java
Object
eval​(
String
script,

ScriptContext
context)
throws
ScriptException
```

Causes the immediate execution of the script whose source is the String
passed as the first argument. The script may be reparsed or recompiled before
execution. State left in the engine from previous executions, including
variable values and compiled procedures may be visible during this execution.

**Parameters:** script

- The script to be executed by the script engine.
**Parameters:** context

- A

ScriptContext

exposing sets of attributes in
different scopes. The meanings of the scopes

ScriptContext.GLOBAL_SCOPE

,
and

ScriptContext.ENGINE_SCOPE

are defined in the specification.

The

ENGINE_SCOPE

Bindings

of the

ScriptContext

contains the
bindings of scripting variables to application objects to be used during this
script execution.
**Returns:** The value returned from the execution of the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

- eval

```java
Object
eval​(
Reader
reader,

ScriptContext
context)
throws
ScriptException
```

Same as

eval(String, ScriptContext)

where the source of the script
is read from a

Reader

.

**Parameters:** reader

- The source of the script to be executed by the script engine.
**Parameters:** context

- The

ScriptContext

passed to the script engine.
**Returns:** The value returned from the execution of the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

- eval

```java
Object
eval​(
String
script)
throws
ScriptException
```

Executes the specified script. The default

ScriptContext

for the

ScriptEngine

is used.

**Parameters:** script

- The script language source to be executed.
**Returns:** The value returned from the execution of the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if the argument is null.

- eval

```java
Object
eval​(
Reader
reader)
throws
ScriptException
```

Same as

eval(String)

except that the source of the script is
provided as a

Reader

**Parameters:** reader

- The source of the script.
**Returns:** The value returned by the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if the argument is null.

- eval

```java
Object
eval​(
String
script,

Bindings
n)
throws
ScriptException
```

Executes the script using the

Bindings

argument as the

ENGINE_SCOPE

Bindings

of the

ScriptEngine

during the script execution. The

Reader

,

Writer

and non-

ENGINE_SCOPE

Bindings

of the
default

ScriptContext

are used. The

ENGINE_SCOPE

Bindings

of the

ScriptEngine

is not changed, and its
mappings are unaltered by the script execution.

**Parameters:** script

- The source for the script.
**Parameters:** n

- The

Bindings

of attributes to be used for script execution.
**Returns:** The value returned by the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

- eval

```java
Object
eval​(
Reader
reader,

Bindings
n)
throws
ScriptException
```

Same as

eval(String, Bindings)

except that the source of the script
is provided as a

Reader

.

**Parameters:** reader

- The source of the script.
**Parameters:** n

- The

Bindings

of attributes.
**Returns:** The value returned by the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

- put

```java
void put​(
String
key,

Object
value)
```

Sets a key/value pair in the state of the ScriptEngine that may either create
a Java Language Binding to be used in the execution of scripts or be used in some
other way, depending on whether the key is reserved. Must have the same effect as

getBindings(ScriptContext.ENGINE_SCOPE).put

.

**Parameters:** key

- The name of named value to add
**Parameters:** value

- The value of named value to add.
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

- get

```java
Object
get​(
String
key)
```

Retrieves a value set in the state of this engine. The value might be one
which was set using

setValue

or some other value in the state
of the

ScriptEngine

, depending on the implementation. Must have the same effect
as

getBindings(ScriptContext.ENGINE_SCOPE).get

**Parameters:** key

- The key whose value is to be returned
**Returns:** the value for the given key
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

- getBindings

```java
Bindings
getBindings​(int scope)
```

Returns a scope of named values. The possible scopes are:

- ScriptContext.GLOBAL_SCOPE

- The set of named values representing global
scope. If this

ScriptEngine

is created by a

ScriptEngineManager

,
then the manager sets global scope bindings. This may be

null

if no global
scope is associated with this

ScriptEngine
- ScriptContext.ENGINE_SCOPE

- The set of named values representing the state of
this

ScriptEngine

. The values are generally visible in scripts using
the associated keys as variable names.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The

Bindings

instances that are returned must be identical to those returned by the

getBindings

method of

ScriptContext

called with corresponding arguments on
the default

ScriptContext

of the

ScriptEngine

.

**Parameters:** scope

- Either

ScriptContext.ENGINE_SCOPE

or

ScriptContext.GLOBAL_SCOPE

which specifies the

Bindings

to return. Implementations of

ScriptContext

may define additional scopes. If the default

ScriptContext

of the

ScriptEngine

defines additional scopes, any of them can be passed to get the corresponding

Bindings

.
**Returns:** The

Bindings

with the specified scope.
**Throws:** IllegalArgumentException

- if specified scope is invalid

- setBindings

```java
void setBindings​(
Bindings
bindings,
int scope)
```

Sets a scope of named values to be used by scripts. The possible scopes are:

- ScriptContext.ENGINE_SCOPE

- The specified

Bindings

replaces the
engine scope of the

ScriptEngine

.
- ScriptContext.GLOBAL_SCOPE

- The specified

Bindings

must be visible
as the

GLOBAL_SCOPE

.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The method must have the same effect as calling the

setBindings

method of

ScriptContext

with the corresponding value of

scope

on the default

ScriptContext

of the

ScriptEngine

.

**Parameters:** bindings

- The

Bindings

for the specified scope.
**Parameters:** scope

- The specified scope. Either

ScriptContext.ENGINE_SCOPE

,

ScriptContext.GLOBAL_SCOPE

, or any other valid value of scope.
**Throws:** IllegalArgumentException

- if the scope is invalid
**Throws:** NullPointerException

- if the bindings is null and the scope is

ScriptContext.ENGINE_SCOPE

- createBindings

```java
Bindings
createBindings()
```

Returns an uninitialized

Bindings

.

**Returns:** A

Bindings

that can be used to replace the state of this

ScriptEngine

.

- getContext

```java
ScriptContext
getContext()
```

Returns the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

**Returns:** The default

ScriptContext

of the

ScriptEngine

.

- setContext

```java
void setContext​(
ScriptContext
context)
```

Sets the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

**Parameters:** context

- A

ScriptContext

that will replace the default

ScriptContext

in
the

ScriptEngine

.
**Throws:** NullPointerException

- if context is null.

- getFactory

```java
ScriptEngineFactory
getFactory()
```

Returns a

ScriptEngineFactory

for the class to which this

ScriptEngine

belongs.

**Returns:** The

ScriptEngineFactory

---

#### Method Detail

eval

```java
Object
eval​(
String
script,

ScriptContext
context)
throws
ScriptException
```

Causes the immediate execution of the script whose source is the String
passed as the first argument. The script may be reparsed or recompiled before
execution. State left in the engine from previous executions, including
variable values and compiled procedures may be visible during this execution.

**Parameters:** script

- The script to be executed by the script engine.
**Parameters:** context

- A

ScriptContext

exposing sets of attributes in
different scopes. The meanings of the scopes

ScriptContext.GLOBAL_SCOPE

,
and

ScriptContext.ENGINE_SCOPE

are defined in the specification.

The

ENGINE_SCOPE

Bindings

of the

ScriptContext

contains the
bindings of scripting variables to application objects to be used during this
script execution.
**Returns:** The value returned from the execution of the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

---

#### eval

Object

eval​(

String

script,

ScriptContext

context)
throws

ScriptException

Causes the immediate execution of the script whose source is the String
passed as the first argument. The script may be reparsed or recompiled before
execution. State left in the engine from previous executions, including
variable values and compiled procedures may be visible during this execution.

eval

```java
Object
eval​(
Reader
reader,

ScriptContext
context)
throws
ScriptException
```

Same as

eval(String, ScriptContext)

where the source of the script
is read from a

Reader

.

**Parameters:** reader

- The source of the script to be executed by the script engine.
**Parameters:** context

- The

ScriptContext

passed to the script engine.
**Returns:** The value returned from the execution of the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

---

#### eval

Object

eval​(

Reader

reader,

ScriptContext

context)
throws

ScriptException

Same as

eval(String, ScriptContext)

where the source of the script
is read from a

Reader

.

eval

```java
Object
eval​(
String
script)
throws
ScriptException
```

Executes the specified script. The default

ScriptContext

for the

ScriptEngine

is used.

**Parameters:** script

- The script language source to be executed.
**Returns:** The value returned from the execution of the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if the argument is null.

---

#### eval

Object

eval​(

String

script)
throws

ScriptException

Executes the specified script. The default

ScriptContext

for the

ScriptEngine

is used.

eval

```java
Object
eval​(
Reader
reader)
throws
ScriptException
```

Same as

eval(String)

except that the source of the script is
provided as a

Reader

**Parameters:** reader

- The source of the script.
**Returns:** The value returned by the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if the argument is null.

---

#### eval

Object

eval​(

Reader

reader)
throws

ScriptException

Same as

eval(String)

except that the source of the script is
provided as a

Reader

eval

```java
Object
eval​(
String
script,

Bindings
n)
throws
ScriptException
```

Executes the script using the

Bindings

argument as the

ENGINE_SCOPE

Bindings

of the

ScriptEngine

during the script execution. The

Reader

,

Writer

and non-

ENGINE_SCOPE

Bindings

of the
default

ScriptContext

are used. The

ENGINE_SCOPE

Bindings

of the

ScriptEngine

is not changed, and its
mappings are unaltered by the script execution.

**Parameters:** script

- The source for the script.
**Parameters:** n

- The

Bindings

of attributes to be used for script execution.
**Returns:** The value returned by the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

---

#### eval

Object

eval​(

String

script,

Bindings

n)
throws

ScriptException

Executes the script using the

Bindings

argument as the

ENGINE_SCOPE

Bindings

of the

ScriptEngine

during the script execution. The

Reader

,

Writer

and non-

ENGINE_SCOPE

Bindings

of the
default

ScriptContext

are used. The

ENGINE_SCOPE

Bindings

of the

ScriptEngine

is not changed, and its
mappings are unaltered by the script execution.

eval

```java
Object
eval​(
Reader
reader,

Bindings
n)
throws
ScriptException
```

Same as

eval(String, Bindings)

except that the source of the script
is provided as a

Reader

.

**Parameters:** reader

- The source of the script.
**Parameters:** n

- The

Bindings

of attributes.
**Returns:** The value returned by the script.
**Throws:** ScriptException

- if an error occurs in script. ScriptEngines should create and throw

ScriptException

wrappers for checked Exceptions thrown by underlying scripting
implementations.
**Throws:** NullPointerException

- if either argument is null.

---

#### eval

Object

eval​(

Reader

reader,

Bindings

n)
throws

ScriptException

Same as

eval(String, Bindings)

except that the source of the script
is provided as a

Reader

.

put

```java
void put​(
String
key,

Object
value)
```

Sets a key/value pair in the state of the ScriptEngine that may either create
a Java Language Binding to be used in the execution of scripts or be used in some
other way, depending on whether the key is reserved. Must have the same effect as

getBindings(ScriptContext.ENGINE_SCOPE).put

.

**Parameters:** key

- The name of named value to add
**Parameters:** value

- The value of named value to add.
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

---

#### put

void put​(

String

key,

Object

value)

Sets a key/value pair in the state of the ScriptEngine that may either create
a Java Language Binding to be used in the execution of scripts or be used in some
other way, depending on whether the key is reserved. Must have the same effect as

getBindings(ScriptContext.ENGINE_SCOPE).put

.

get

```java
Object
get​(
String
key)
```

Retrieves a value set in the state of this engine. The value might be one
which was set using

setValue

or some other value in the state
of the

ScriptEngine

, depending on the implementation. Must have the same effect
as

getBindings(ScriptContext.ENGINE_SCOPE).get

**Parameters:** key

- The key whose value is to be returned
**Returns:** the value for the given key
**Throws:** NullPointerException

- if key is null.
**Throws:** IllegalArgumentException

- if key is empty.

---

#### get

Object

get​(

String

key)

Retrieves a value set in the state of this engine. The value might be one
which was set using

setValue

or some other value in the state
of the

ScriptEngine

, depending on the implementation. Must have the same effect
as

getBindings(ScriptContext.ENGINE_SCOPE).get

getBindings

```java
Bindings
getBindings​(int scope)
```

Returns a scope of named values. The possible scopes are:

- ScriptContext.GLOBAL_SCOPE

- The set of named values representing global
scope. If this

ScriptEngine

is created by a

ScriptEngineManager

,
then the manager sets global scope bindings. This may be

null

if no global
scope is associated with this

ScriptEngine
- ScriptContext.ENGINE_SCOPE

- The set of named values representing the state of
this

ScriptEngine

. The values are generally visible in scripts using
the associated keys as variable names.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The

Bindings

instances that are returned must be identical to those returned by the

getBindings

method of

ScriptContext

called with corresponding arguments on
the default

ScriptContext

of the

ScriptEngine

.

**Parameters:** scope

- Either

ScriptContext.ENGINE_SCOPE

or

ScriptContext.GLOBAL_SCOPE

which specifies the

Bindings

to return. Implementations of

ScriptContext

may define additional scopes. If the default

ScriptContext

of the

ScriptEngine

defines additional scopes, any of them can be passed to get the corresponding

Bindings

.
**Returns:** The

Bindings

with the specified scope.
**Throws:** IllegalArgumentException

- if specified scope is invalid

---

#### getBindings

Bindings

getBindings​(int scope)

Returns a scope of named values. The possible scopes are:

- ScriptContext.GLOBAL_SCOPE

- The set of named values representing global
scope. If this

ScriptEngine

is created by a

ScriptEngineManager

,
then the manager sets global scope bindings. This may be

null

if no global
scope is associated with this

ScriptEngine
- ScriptContext.ENGINE_SCOPE

- The set of named values representing the state of
this

ScriptEngine

. The values are generally visible in scripts using
the associated keys as variable names.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The

Bindings

instances that are returned must be identical to those returned by the

getBindings

method of

ScriptContext

called with corresponding arguments on
the default

ScriptContext

of the

ScriptEngine

.

ScriptContext.GLOBAL_SCOPE

- The set of named values representing global
scope. If this

ScriptEngine

is created by a

ScriptEngineManager

,
then the manager sets global scope bindings. This may be

null

if no global
scope is associated with this

ScriptEngine

ScriptContext.ENGINE_SCOPE

- The set of named values representing the state of
this

ScriptEngine

. The values are generally visible in scripts using
the associated keys as variable names.

Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

setBindings

```java
void setBindings​(
Bindings
bindings,
int scope)
```

Sets a scope of named values to be used by scripts. The possible scopes are:

- ScriptContext.ENGINE_SCOPE

- The specified

Bindings

replaces the
engine scope of the

ScriptEngine

.
- ScriptContext.GLOBAL_SCOPE

- The specified

Bindings

must be visible
as the

GLOBAL_SCOPE

.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The method must have the same effect as calling the

setBindings

method of

ScriptContext

with the corresponding value of

scope

on the default

ScriptContext

of the

ScriptEngine

.

**Parameters:** bindings

- The

Bindings

for the specified scope.
**Parameters:** scope

- The specified scope. Either

ScriptContext.ENGINE_SCOPE

,

ScriptContext.GLOBAL_SCOPE

, or any other valid value of scope.
**Throws:** IllegalArgumentException

- if the scope is invalid
**Throws:** NullPointerException

- if the bindings is null and the scope is

ScriptContext.ENGINE_SCOPE

---

#### setBindings

void setBindings​(

Bindings

bindings,
int scope)

Sets a scope of named values to be used by scripts. The possible scopes are:

- ScriptContext.ENGINE_SCOPE

- The specified

Bindings

replaces the
engine scope of the

ScriptEngine

.
- ScriptContext.GLOBAL_SCOPE

- The specified

Bindings

must be visible
as the

GLOBAL_SCOPE

.
- Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

The method must have the same effect as calling the

setBindings

method of

ScriptContext

with the corresponding value of

scope

on the default

ScriptContext

of the

ScriptEngine

.

ScriptContext.ENGINE_SCOPE

- The specified

Bindings

replaces the
engine scope of the

ScriptEngine

.

ScriptContext.GLOBAL_SCOPE

- The specified

Bindings

must be visible
as the

GLOBAL_SCOPE

.

Any other value of scope defined in the default

ScriptContext

of the

ScriptEngine

.

createBindings

```java
Bindings
createBindings()
```

Returns an uninitialized

Bindings

.

**Returns:** A

Bindings

that can be used to replace the state of this

ScriptEngine

.

---

#### createBindings

Bindings

createBindings()

Returns an uninitialized

Bindings

.

getContext

```java
ScriptContext
getContext()
```

Returns the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

**Returns:** The default

ScriptContext

of the

ScriptEngine

.

---

#### getContext

ScriptContext

getContext()

Returns the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

setContext

```java
void setContext​(
ScriptContext
context)
```

Sets the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

**Parameters:** context

- A

ScriptContext

that will replace the default

ScriptContext

in
the

ScriptEngine

.
**Throws:** NullPointerException

- if context is null.

---

#### setContext

void setContext​(

ScriptContext

context)

Sets the default

ScriptContext

of the

ScriptEngine

whose Bindings, Reader
and Writers are used for script executions when no

ScriptContext

is specified.

getFactory

```java
ScriptEngineFactory
getFactory()
```

Returns a

ScriptEngineFactory

for the class to which this

ScriptEngine

belongs.

**Returns:** The

ScriptEngineFactory

---

#### getFactory

ScriptEngineFactory

getFactory()

Returns a

ScriptEngineFactory

for the class to which this

ScriptEngine

belongs.

---

