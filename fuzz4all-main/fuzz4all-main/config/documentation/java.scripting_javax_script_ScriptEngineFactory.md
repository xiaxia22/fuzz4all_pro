# Interface ScriptEngineFactory

**Source:** `java.scripting\javax\script\ScriptEngineFactory.html`

### Class Description

```java
public interface
ScriptEngineFactory
```

ScriptEngineFactory

is used to describe and instantiate

ScriptEngines

.

Each class implementing

ScriptEngine

has a corresponding
factory that exposes metadata describing the engine class.

The

ScriptEngineManager

uses the service-provider loader mechanism described in the

ServiceLoader

class to obtain
instances of

ScriptEngineFactory

instances.
See

ScriptEngineManager()

and

ScriptEngineManager(java.lang.ClassLoader)

.

**All Known Implementing Classes:** NashornScriptEngineFactory

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getEngineName()

Returns the full name of the

ScriptEngine

. For
instance an implementation based on the Mozilla Rhino Javascript engine
might return

Rhino Mozilla Javascript Engine

.

**Returns:**
- The name of the engine implementation.

---

#### String
getEngineVersion()

Returns the version of the

ScriptEngine

.

**Returns:**
- The

ScriptEngine

implementation version.

---

#### List
<
String
> getExtensions()

Returns an immutable list of filename extensions, which generally identify scripts
written in the language supported by this

ScriptEngine

.
The array is used by the

ScriptEngineManager

to implement its

getEngineByExtension

method.

**Returns:**
- The list of extensions.

---

#### List
<
String
> getMimeTypes()

Returns an immutable list of mimetypes, associated with scripts that
can be executed by the engine. The list is used by the

ScriptEngineManager

class to implement its

getEngineByMimetype

method.

**Returns:**
- The list of mime types.

---

#### List
<
String
> getNames()

Returns an immutable list of short names for the

ScriptEngine

, which may be used to
identify the

ScriptEngine

by the

ScriptEngineManager

.
For instance, an implementation based on the Mozilla Rhino Javascript engine might
return list containing {"javascript", "rhino"}.

**Returns:**
- an immutable list of short names

---

#### String
getLanguageName()

Returns the name of the scripting language supported by this

ScriptEngine

.

**Returns:**
- The name of the supported language.

---

#### String
getLanguageVersion()

Returns the version of the scripting language supported by this

ScriptEngine

.

**Returns:**
- The version of the supported language.

---

#### Object
getParameter​(
String
key)

Returns the value of an attribute whose meaning may be implementation-specific.
Keys for which the value is defined in all implementations are:

- ScriptEngine.ENGINE
- ScriptEngine.ENGINE_VERSION
- ScriptEngine.LANGUAGE
- ScriptEngine.LANGUAGE_VERSION
- ScriptEngine.NAME

The values for these keys are the Strings returned by

getEngineName

,

getEngineVersion

,

getLanguageName

,

getLanguageVersion

for the first four keys respectively. For NAME, one of the Strings
returned by

getNames

is returned.

A reserved key,

THREADING

, whose value describes the behavior of the engine
with respect to concurrent execution of scripts and maintenance of state is also defined.
These values for the

THREADING

key are:

- null

- The engine implementation is not thread safe, and cannot
be used to execute scripts concurrently on multiple threads.

"MULTITHREADED"

- The engine implementation is internally
thread-safe and scripts may execute concurrently although effects of script execution
on one thread may be visible to scripts on other threads.

"THREAD-ISOLATED"

- The implementation satisfies the requirements
of "MULTITHREADED", and also, the engine maintains independent values
for symbols in scripts executing on different threads.

"STATELESS"

- The implementation satisfies the requirements of

"THREAD-ISOLATED"

. In addition, script executions do not alter the
mappings in the

Bindings

which is the engine scope of the

ScriptEngine

. In particular, the keys in the

Bindings

and their associated values are the same before and after the execution of the script.

Implementations may define implementation-specific keys.

**Parameters:**
- key

- The name of the parameter

**Returns:**
- The value for the given parameter. Returns

null

if no
value is assigned to the key.

**Throws:**
- NullPointerException

- if the key is null.

---

#### String
getMethodCallSyntax​(
String
obj,

String
m,

String
... args)

Returns a String which can be used to invoke a method of a Java object using the syntax
of the supported scripting language. For instance, an implementation for a Javascript
engine might be;

```java
public String getMethodCallSyntax(String obj,
String m, String... args) {
String ret = obj;
ret += "." + m + "(";
for (int i = 0; i < args.length; i++) {
ret += args[i];
if (i < args.length - 1) {
ret += ",";
}
}
ret += ")";
return ret;
}
```

**Parameters:**
- obj

- The name representing the object whose method is to be invoked. The
name is the one used to create bindings using the

put

method of

ScriptEngine

, the

put

method of an

ENGINE_SCOPE

Bindings

,or the

setAttribute

method
of

ScriptContext

. The identifier used in scripts may be a decorated form of the
specified one.
- m

- The name of the method to invoke.
- args

- names of the arguments in the method call.

**Returns:**
- The String used to invoke the method in the syntax of the scripting language.

**Throws:**
- NullPointerException

- if obj or m or args or any of the elements of args is null.

---

#### String
getOutputStatement​(
String
toDisplay)

Returns a String that can be used as a statement to display the specified String using
the syntax of the supported scripting language. For instance, the implementation for a Perl
engine might be;

```java
public String getOutputStatement(String toDisplay) {
return "print(" + toDisplay + ")";
}
```

**Parameters:**
- toDisplay

- The String to be displayed by the returned statement.

**Returns:**
- The string used to display the String in the syntax of the scripting language.

---

#### String
getProgram​(
String
... statements)

Returns a valid scripting language executable program with given statements.
For instance an implementation for a PHP engine might be:

```java
public String getProgram(String... statements) {
String retval = "<?\n";
int len = statements.length;
for (int i = 0; i < len; i++) {
retval += statements[i] + ";\n";
}
return retval += "?>";
}
```

**Parameters:**
- statements

- The statements to be executed. May be return values of
calls to the

getMethodCallSyntax

and

getOutputStatement

methods.

**Returns:**
- The Program

**Throws:**
- NullPointerException

- if the

statements

array or any of its elements is null

---

#### ScriptEngine
getScriptEngine()

Returns an instance of the

ScriptEngine

associated with this

ScriptEngineFactory

. A new ScriptEngine is generally
returned, but implementations may pool, share or reuse engines.

**Returns:**
- A new

ScriptEngine

instance.

---

### Additional Sections

#### Interface ScriptEngineFactory

**All Known Implementing Classes:** NashornScriptEngineFactory

```java
public interface
ScriptEngineFactory
```

ScriptEngineFactory

is used to describe and instantiate

ScriptEngines

.

Each class implementing

ScriptEngine

has a corresponding
factory that exposes metadata describing the engine class.

The

ScriptEngineManager

uses the service-provider loader mechanism described in the

ServiceLoader

class to obtain
instances of

ScriptEngineFactory

instances.
See

ScriptEngineManager()

and

ScriptEngineManager(java.lang.ClassLoader)

.

**Since:** 1.6

public interface

ScriptEngineFactory

ScriptEngineFactory

is used to describe and instantiate

ScriptEngines

.

Each class implementing

ScriptEngine

has a corresponding
factory that exposes metadata describing the engine class.

The

ScriptEngineManager

uses the service-provider loader mechanism described in the

ServiceLoader

class to obtain
instances of

ScriptEngineFactory

instances.
See

ScriptEngineManager()

and

ScriptEngineManager(java.lang.ClassLoader)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getEngineName

()

Returns the full name of the

ScriptEngine

.

String

getEngineVersion

()

Returns the version of the

ScriptEngine

.

List

<

String

>

getExtensions

()

Returns an immutable list of filename extensions, which generally identify scripts
written in the language supported by this

ScriptEngine

.

String

getLanguageName

()

Returns the name of the scripting language supported by this

ScriptEngine

.

String

getLanguageVersion

()

Returns the version of the scripting language supported by this

ScriptEngine

.

String

getMethodCallSyntax

​(

String

obj,

String

m,

String

... args)

Returns a String which can be used to invoke a method of a Java object using the syntax
of the supported scripting language.

List

<

String

>

getMimeTypes

()

Returns an immutable list of mimetypes, associated with scripts that
can be executed by the engine.

List

<

String

>

getNames

()

Returns an immutable list of short names for the

ScriptEngine

, which may be used to
identify the

ScriptEngine

by the

ScriptEngineManager

.

String

getOutputStatement

​(

String

toDisplay)

Returns a String that can be used as a statement to display the specified String using
the syntax of the supported scripting language.

Object

getParameter

​(

String

key)

Returns the value of an attribute whose meaning may be implementation-specific.

String

getProgram

​(

String

... statements)

Returns a valid scripting language executable program with given statements.

ScriptEngine

getScriptEngine

()

Returns an instance of the

ScriptEngine

associated with this

ScriptEngineFactory

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getEngineName

()

Returns the full name of the

ScriptEngine

.

String

getEngineVersion

()

Returns the version of the

ScriptEngine

.

List

<

String

>

getExtensions

()

Returns an immutable list of filename extensions, which generally identify scripts
written in the language supported by this

ScriptEngine

.

String

getLanguageName

()

Returns the name of the scripting language supported by this

ScriptEngine

.

String

getLanguageVersion

()

Returns the version of the scripting language supported by this

ScriptEngine

.

String

getMethodCallSyntax

​(

String

obj,

String

m,

String

... args)

Returns a String which can be used to invoke a method of a Java object using the syntax
of the supported scripting language.

List

<

String

>

getMimeTypes

()

Returns an immutable list of mimetypes, associated with scripts that
can be executed by the engine.

List

<

String

>

getNames

()

Returns an immutable list of short names for the

ScriptEngine

, which may be used to
identify the

ScriptEngine

by the

ScriptEngineManager

.

String

getOutputStatement

​(

String

toDisplay)

Returns a String that can be used as a statement to display the specified String using
the syntax of the supported scripting language.

Object

getParameter

​(

String

key)

Returns the value of an attribute whose meaning may be implementation-specific.

String

getProgram

​(

String

... statements)

Returns a valid scripting language executable program with given statements.

ScriptEngine

getScriptEngine

()

Returns an instance of the

ScriptEngine

associated with this

ScriptEngineFactory

.

---

#### Method Summary

Returns the full name of the

ScriptEngine

.

Returns the version of the

ScriptEngine

.

Returns an immutable list of filename extensions, which generally identify scripts
written in the language supported by this

ScriptEngine

.

Returns the name of the scripting language supported by this

ScriptEngine

.

Returns the version of the scripting language supported by this

ScriptEngine

.

Returns a String which can be used to invoke a method of a Java object using the syntax
of the supported scripting language.

Returns an immutable list of mimetypes, associated with scripts that
can be executed by the engine.

Returns an immutable list of short names for the

ScriptEngine

, which may be used to
identify the

ScriptEngine

by the

ScriptEngineManager

.

Returns a String that can be used as a statement to display the specified String using
the syntax of the supported scripting language.

Returns the value of an attribute whose meaning may be implementation-specific.

Returns a valid scripting language executable program with given statements.

Returns an instance of the

ScriptEngine

associated with this

ScriptEngineFactory

.

============ METHOD DETAIL ==========

- Method Detail

- getEngineName

```java
String
getEngineName()
```

Returns the full name of the

ScriptEngine

. For
instance an implementation based on the Mozilla Rhino Javascript engine
might return

Rhino Mozilla Javascript Engine

.

**Returns:** The name of the engine implementation.

- getEngineVersion

```java
String
getEngineVersion()
```

Returns the version of the

ScriptEngine

.

**Returns:** The

ScriptEngine

implementation version.

- getExtensions

```java
List
<
String
> getExtensions()
```

Returns an immutable list of filename extensions, which generally identify scripts
written in the language supported by this

ScriptEngine

.
The array is used by the

ScriptEngineManager

to implement its

getEngineByExtension

method.

**Returns:** The list of extensions.

- getMimeTypes

```java
List
<
String
> getMimeTypes()
```

Returns an immutable list of mimetypes, associated with scripts that
can be executed by the engine. The list is used by the

ScriptEngineManager

class to implement its

getEngineByMimetype

method.

**Returns:** The list of mime types.

- getNames

```java
List
<
String
> getNames()
```

Returns an immutable list of short names for the

ScriptEngine

, which may be used to
identify the

ScriptEngine

by the

ScriptEngineManager

.
For instance, an implementation based on the Mozilla Rhino Javascript engine might
return list containing {"javascript", "rhino"}.

**Returns:** an immutable list of short names

- getLanguageName

```java
String
getLanguageName()
```

Returns the name of the scripting language supported by this

ScriptEngine

.

**Returns:** The name of the supported language.

- getLanguageVersion

```java
String
getLanguageVersion()
```

Returns the version of the scripting language supported by this

ScriptEngine

.

**Returns:** The version of the supported language.

- getParameter

```java
Object
getParameter​(
String
key)
```

Returns the value of an attribute whose meaning may be implementation-specific.
Keys for which the value is defined in all implementations are:

- ScriptEngine.ENGINE
- ScriptEngine.ENGINE_VERSION
- ScriptEngine.LANGUAGE
- ScriptEngine.LANGUAGE_VERSION
- ScriptEngine.NAME

The values for these keys are the Strings returned by

getEngineName

,

getEngineVersion

,

getLanguageName

,

getLanguageVersion

for the first four keys respectively. For NAME, one of the Strings
returned by

getNames

is returned.

A reserved key,

THREADING

, whose value describes the behavior of the engine
with respect to concurrent execution of scripts and maintenance of state is also defined.
These values for the

THREADING

key are:

- null

- The engine implementation is not thread safe, and cannot
be used to execute scripts concurrently on multiple threads.

"MULTITHREADED"

- The engine implementation is internally
thread-safe and scripts may execute concurrently although effects of script execution
on one thread may be visible to scripts on other threads.

"THREAD-ISOLATED"

- The implementation satisfies the requirements
of "MULTITHREADED", and also, the engine maintains independent values
for symbols in scripts executing on different threads.

"STATELESS"

- The implementation satisfies the requirements of

"THREAD-ISOLATED"

. In addition, script executions do not alter the
mappings in the

Bindings

which is the engine scope of the

ScriptEngine

. In particular, the keys in the

Bindings

and their associated values are the same before and after the execution of the script.

Implementations may define implementation-specific keys.

**Parameters:** key

- The name of the parameter
**Returns:** The value for the given parameter. Returns

null

if no
value is assigned to the key.
**Throws:** NullPointerException

- if the key is null.

- getMethodCallSyntax

```java
String
getMethodCallSyntax​(
String
obj,

String
m,

String
... args)
```

Returns a String which can be used to invoke a method of a Java object using the syntax
of the supported scripting language. For instance, an implementation for a Javascript
engine might be;

```java
public String getMethodCallSyntax(String obj,
String m, String... args) {
String ret = obj;
ret += "." + m + "(";
for (int i = 0; i < args.length; i++) {
ret += args[i];
if (i < args.length - 1) {
ret += ",";
}
}
ret += ")";
return ret;
}
```

**Parameters:** obj

- The name representing the object whose method is to be invoked. The
name is the one used to create bindings using the

put

method of

ScriptEngine

, the

put

method of an

ENGINE_SCOPE

Bindings

,or the

setAttribute

method
of

ScriptContext

. The identifier used in scripts may be a decorated form of the
specified one.
**Parameters:** m

- The name of the method to invoke.
**Parameters:** args

- names of the arguments in the method call.
**Returns:** The String used to invoke the method in the syntax of the scripting language.
**Throws:** NullPointerException

- if obj or m or args or any of the elements of args is null.

- getOutputStatement

```java
String
getOutputStatement​(
String
toDisplay)
```

Returns a String that can be used as a statement to display the specified String using
the syntax of the supported scripting language. For instance, the implementation for a Perl
engine might be;

```java
public String getOutputStatement(String toDisplay) {
return "print(" + toDisplay + ")";
}
```

**Parameters:** toDisplay

- The String to be displayed by the returned statement.
**Returns:** The string used to display the String in the syntax of the scripting language.

- getProgram

```java
String
getProgram​(
String
... statements)
```

Returns a valid scripting language executable program with given statements.
For instance an implementation for a PHP engine might be:

```java
public String getProgram(String... statements) {
String retval = "<?\n";
int len = statements.length;
for (int i = 0; i < len; i++) {
retval += statements[i] + ";\n";
}
return retval += "?>";
}
```

**Parameters:** statements

- The statements to be executed. May be return values of
calls to the

getMethodCallSyntax

and

getOutputStatement

methods.
**Returns:** The Program
**Throws:** NullPointerException

- if the

statements

array or any of its elements is null

- getScriptEngine

```java
ScriptEngine
getScriptEngine()
```

Returns an instance of the

ScriptEngine

associated with this

ScriptEngineFactory

. A new ScriptEngine is generally
returned, but implementations may pool, share or reuse engines.

**Returns:** A new

ScriptEngine

instance.

Method Detail

- getEngineName

```java
String
getEngineName()
```

Returns the full name of the

ScriptEngine

. For
instance an implementation based on the Mozilla Rhino Javascript engine
might return

Rhino Mozilla Javascript Engine

.

**Returns:** The name of the engine implementation.

- getEngineVersion

```java
String
getEngineVersion()
```

Returns the version of the

ScriptEngine

.

**Returns:** The

ScriptEngine

implementation version.

- getExtensions

```java
List
<
String
> getExtensions()
```

Returns an immutable list of filename extensions, which generally identify scripts
written in the language supported by this

ScriptEngine

.
The array is used by the

ScriptEngineManager

to implement its

getEngineByExtension

method.

**Returns:** The list of extensions.

- getMimeTypes

```java
List
<
String
> getMimeTypes()
```

Returns an immutable list of mimetypes, associated with scripts that
can be executed by the engine. The list is used by the

ScriptEngineManager

class to implement its

getEngineByMimetype

method.

**Returns:** The list of mime types.

- getNames

```java
List
<
String
> getNames()
```

Returns an immutable list of short names for the

ScriptEngine

, which may be used to
identify the

ScriptEngine

by the

ScriptEngineManager

.
For instance, an implementation based on the Mozilla Rhino Javascript engine might
return list containing {"javascript", "rhino"}.

**Returns:** an immutable list of short names

- getLanguageName

```java
String
getLanguageName()
```

Returns the name of the scripting language supported by this

ScriptEngine

.

**Returns:** The name of the supported language.

- getLanguageVersion

```java
String
getLanguageVersion()
```

Returns the version of the scripting language supported by this

ScriptEngine

.

**Returns:** The version of the supported language.

- getParameter

```java
Object
getParameter​(
String
key)
```

Returns the value of an attribute whose meaning may be implementation-specific.
Keys for which the value is defined in all implementations are:

- ScriptEngine.ENGINE
- ScriptEngine.ENGINE_VERSION
- ScriptEngine.LANGUAGE
- ScriptEngine.LANGUAGE_VERSION
- ScriptEngine.NAME

The values for these keys are the Strings returned by

getEngineName

,

getEngineVersion

,

getLanguageName

,

getLanguageVersion

for the first four keys respectively. For NAME, one of the Strings
returned by

getNames

is returned.

A reserved key,

THREADING

, whose value describes the behavior of the engine
with respect to concurrent execution of scripts and maintenance of state is also defined.
These values for the

THREADING

key are:

- null

- The engine implementation is not thread safe, and cannot
be used to execute scripts concurrently on multiple threads.

"MULTITHREADED"

- The engine implementation is internally
thread-safe and scripts may execute concurrently although effects of script execution
on one thread may be visible to scripts on other threads.

"THREAD-ISOLATED"

- The implementation satisfies the requirements
of "MULTITHREADED", and also, the engine maintains independent values
for symbols in scripts executing on different threads.

"STATELESS"

- The implementation satisfies the requirements of

"THREAD-ISOLATED"

. In addition, script executions do not alter the
mappings in the

Bindings

which is the engine scope of the

ScriptEngine

. In particular, the keys in the

Bindings

and their associated values are the same before and after the execution of the script.

Implementations may define implementation-specific keys.

**Parameters:** key

- The name of the parameter
**Returns:** The value for the given parameter. Returns

null

if no
value is assigned to the key.
**Throws:** NullPointerException

- if the key is null.

- getMethodCallSyntax

```java
String
getMethodCallSyntax​(
String
obj,

String
m,

String
... args)
```

Returns a String which can be used to invoke a method of a Java object using the syntax
of the supported scripting language. For instance, an implementation for a Javascript
engine might be;

```java
public String getMethodCallSyntax(String obj,
String m, String... args) {
String ret = obj;
ret += "." + m + "(";
for (int i = 0; i < args.length; i++) {
ret += args[i];
if (i < args.length - 1) {
ret += ",";
}
}
ret += ")";
return ret;
}
```

**Parameters:** obj

- The name representing the object whose method is to be invoked. The
name is the one used to create bindings using the

put

method of

ScriptEngine

, the

put

method of an

ENGINE_SCOPE

Bindings

,or the

setAttribute

method
of

ScriptContext

. The identifier used in scripts may be a decorated form of the
specified one.
**Parameters:** m

- The name of the method to invoke.
**Parameters:** args

- names of the arguments in the method call.
**Returns:** The String used to invoke the method in the syntax of the scripting language.
**Throws:** NullPointerException

- if obj or m or args or any of the elements of args is null.

- getOutputStatement

```java
String
getOutputStatement​(
String
toDisplay)
```

Returns a String that can be used as a statement to display the specified String using
the syntax of the supported scripting language. For instance, the implementation for a Perl
engine might be;

```java
public String getOutputStatement(String toDisplay) {
return "print(" + toDisplay + ")";
}
```

**Parameters:** toDisplay

- The String to be displayed by the returned statement.
**Returns:** The string used to display the String in the syntax of the scripting language.

- getProgram

```java
String
getProgram​(
String
... statements)
```

Returns a valid scripting language executable program with given statements.
For instance an implementation for a PHP engine might be:

```java
public String getProgram(String... statements) {
String retval = "<?\n";
int len = statements.length;
for (int i = 0; i < len; i++) {
retval += statements[i] + ";\n";
}
return retval += "?>";
}
```

**Parameters:** statements

- The statements to be executed. May be return values of
calls to the

getMethodCallSyntax

and

getOutputStatement

methods.
**Returns:** The Program
**Throws:** NullPointerException

- if the

statements

array or any of its elements is null

- getScriptEngine

```java
ScriptEngine
getScriptEngine()
```

Returns an instance of the

ScriptEngine

associated with this

ScriptEngineFactory

. A new ScriptEngine is generally
returned, but implementations may pool, share or reuse engines.

**Returns:** A new

ScriptEngine

instance.

---

#### Method Detail

getEngineName

```java
String
getEngineName()
```

Returns the full name of the

ScriptEngine

. For
instance an implementation based on the Mozilla Rhino Javascript engine
might return

Rhino Mozilla Javascript Engine

.

**Returns:** The name of the engine implementation.

---

#### getEngineName

String

getEngineName()

Returns the full name of the

ScriptEngine

. For
instance an implementation based on the Mozilla Rhino Javascript engine
might return

Rhino Mozilla Javascript Engine

.

getEngineVersion

```java
String
getEngineVersion()
```

Returns the version of the

ScriptEngine

.

**Returns:** The

ScriptEngine

implementation version.

---

#### getEngineVersion

String

getEngineVersion()

Returns the version of the

ScriptEngine

.

getExtensions

```java
List
<
String
> getExtensions()
```

Returns an immutable list of filename extensions, which generally identify scripts
written in the language supported by this

ScriptEngine

.
The array is used by the

ScriptEngineManager

to implement its

getEngineByExtension

method.

**Returns:** The list of extensions.

---

#### getExtensions

List

<

String

> getExtensions()

Returns an immutable list of filename extensions, which generally identify scripts
written in the language supported by this

ScriptEngine

.
The array is used by the

ScriptEngineManager

to implement its

getEngineByExtension

method.

getMimeTypes

```java
List
<
String
> getMimeTypes()
```

Returns an immutable list of mimetypes, associated with scripts that
can be executed by the engine. The list is used by the

ScriptEngineManager

class to implement its

getEngineByMimetype

method.

**Returns:** The list of mime types.

---

#### getMimeTypes

List

<

String

> getMimeTypes()

Returns an immutable list of mimetypes, associated with scripts that
can be executed by the engine. The list is used by the

ScriptEngineManager

class to implement its

getEngineByMimetype

method.

getNames

```java
List
<
String
> getNames()
```

Returns an immutable list of short names for the

ScriptEngine

, which may be used to
identify the

ScriptEngine

by the

ScriptEngineManager

.
For instance, an implementation based on the Mozilla Rhino Javascript engine might
return list containing {"javascript", "rhino"}.

**Returns:** an immutable list of short names

---

#### getNames

List

<

String

> getNames()

Returns an immutable list of short names for the

ScriptEngine

, which may be used to
identify the

ScriptEngine

by the

ScriptEngineManager

.
For instance, an implementation based on the Mozilla Rhino Javascript engine might
return list containing {"javascript", "rhino"}.

getLanguageName

```java
String
getLanguageName()
```

Returns the name of the scripting language supported by this

ScriptEngine

.

**Returns:** The name of the supported language.

---

#### getLanguageName

String

getLanguageName()

Returns the name of the scripting language supported by this

ScriptEngine

.

getLanguageVersion

```java
String
getLanguageVersion()
```

Returns the version of the scripting language supported by this

ScriptEngine

.

**Returns:** The version of the supported language.

---

#### getLanguageVersion

String

getLanguageVersion()

Returns the version of the scripting language supported by this

ScriptEngine

.

getParameter

```java
Object
getParameter​(
String
key)
```

Returns the value of an attribute whose meaning may be implementation-specific.
Keys for which the value is defined in all implementations are:

- ScriptEngine.ENGINE
- ScriptEngine.ENGINE_VERSION
- ScriptEngine.LANGUAGE
- ScriptEngine.LANGUAGE_VERSION
- ScriptEngine.NAME

The values for these keys are the Strings returned by

getEngineName

,

getEngineVersion

,

getLanguageName

,

getLanguageVersion

for the first four keys respectively. For NAME, one of the Strings
returned by

getNames

is returned.

A reserved key,

THREADING

, whose value describes the behavior of the engine
with respect to concurrent execution of scripts and maintenance of state is also defined.
These values for the

THREADING

key are:

- null

- The engine implementation is not thread safe, and cannot
be used to execute scripts concurrently on multiple threads.

"MULTITHREADED"

- The engine implementation is internally
thread-safe and scripts may execute concurrently although effects of script execution
on one thread may be visible to scripts on other threads.

"THREAD-ISOLATED"

- The implementation satisfies the requirements
of "MULTITHREADED", and also, the engine maintains independent values
for symbols in scripts executing on different threads.

"STATELESS"

- The implementation satisfies the requirements of

"THREAD-ISOLATED"

. In addition, script executions do not alter the
mappings in the

Bindings

which is the engine scope of the

ScriptEngine

. In particular, the keys in the

Bindings

and their associated values are the same before and after the execution of the script.

Implementations may define implementation-specific keys.

**Parameters:** key

- The name of the parameter
**Returns:** The value for the given parameter. Returns

null

if no
value is assigned to the key.
**Throws:** NullPointerException

- if the key is null.

---

#### getParameter

Object

getParameter​(

String

key)

Returns the value of an attribute whose meaning may be implementation-specific.
Keys for which the value is defined in all implementations are:

- ScriptEngine.ENGINE
- ScriptEngine.ENGINE_VERSION
- ScriptEngine.LANGUAGE
- ScriptEngine.LANGUAGE_VERSION
- ScriptEngine.NAME

The values for these keys are the Strings returned by

getEngineName

,

getEngineVersion

,

getLanguageName

,

getLanguageVersion

for the first four keys respectively. For NAME, one of the Strings
returned by

getNames

is returned.

A reserved key,

THREADING

, whose value describes the behavior of the engine
with respect to concurrent execution of scripts and maintenance of state is also defined.
These values for the

THREADING

key are:

- null

- The engine implementation is not thread safe, and cannot
be used to execute scripts concurrently on multiple threads.

"MULTITHREADED"

- The engine implementation is internally
thread-safe and scripts may execute concurrently although effects of script execution
on one thread may be visible to scripts on other threads.

"THREAD-ISOLATED"

- The implementation satisfies the requirements
of "MULTITHREADED", and also, the engine maintains independent values
for symbols in scripts executing on different threads.

"STATELESS"

- The implementation satisfies the requirements of

"THREAD-ISOLATED"

. In addition, script executions do not alter the
mappings in the

Bindings

which is the engine scope of the

ScriptEngine

. In particular, the keys in the

Bindings

and their associated values are the same before and after the execution of the script.

Implementations may define implementation-specific keys.

ScriptEngine.ENGINE

ScriptEngine.ENGINE_VERSION

ScriptEngine.LANGUAGE

ScriptEngine.LANGUAGE_VERSION

ScriptEngine.NAME

The values for these keys are the Strings returned by

getEngineName

,

getEngineVersion

,

getLanguageName

,

getLanguageVersion

for the first four keys respectively. For NAME, one of the Strings
returned by

getNames

is returned.

A reserved key,

THREADING

, whose value describes the behavior of the engine
with respect to concurrent execution of scripts and maintenance of state is also defined.
These values for the

THREADING

key are:

- null

- The engine implementation is not thread safe, and cannot
be used to execute scripts concurrently on multiple threads.

"MULTITHREADED"

- The engine implementation is internally
thread-safe and scripts may execute concurrently although effects of script execution
on one thread may be visible to scripts on other threads.

"THREAD-ISOLATED"

- The implementation satisfies the requirements
of "MULTITHREADED", and also, the engine maintains independent values
for symbols in scripts executing on different threads.

"STATELESS"

- The implementation satisfies the requirements of

"THREAD-ISOLATED"

. In addition, script executions do not alter the
mappings in the

Bindings

which is the engine scope of the

ScriptEngine

. In particular, the keys in the

Bindings

and their associated values are the same before and after the execution of the script.

Implementations may define implementation-specific keys.

null

- The engine implementation is not thread safe, and cannot
be used to execute scripts concurrently on multiple threads.

"MULTITHREADED"

- The engine implementation is internally
thread-safe and scripts may execute concurrently although effects of script execution
on one thread may be visible to scripts on other threads.

"THREAD-ISOLATED"

- The implementation satisfies the requirements
of "MULTITHREADED", and also, the engine maintains independent values
for symbols in scripts executing on different threads.

"STATELESS"

- The implementation satisfies the requirements of

"THREAD-ISOLATED"

. In addition, script executions do not alter the
mappings in the

Bindings

which is the engine scope of the

ScriptEngine

. In particular, the keys in the

Bindings

and their associated values are the same before and after the execution of the script.

getMethodCallSyntax

```java
String
getMethodCallSyntax​(
String
obj,

String
m,

String
... args)
```

Returns a String which can be used to invoke a method of a Java object using the syntax
of the supported scripting language. For instance, an implementation for a Javascript
engine might be;

```java
public String getMethodCallSyntax(String obj,
String m, String... args) {
String ret = obj;
ret += "." + m + "(";
for (int i = 0; i < args.length; i++) {
ret += args[i];
if (i < args.length - 1) {
ret += ",";
}
}
ret += ")";
return ret;
}
```

**Parameters:** obj

- The name representing the object whose method is to be invoked. The
name is the one used to create bindings using the

put

method of

ScriptEngine

, the

put

method of an

ENGINE_SCOPE

Bindings

,or the

setAttribute

method
of

ScriptContext

. The identifier used in scripts may be a decorated form of the
specified one.
**Parameters:** m

- The name of the method to invoke.
**Parameters:** args

- names of the arguments in the method call.
**Returns:** The String used to invoke the method in the syntax of the scripting language.
**Throws:** NullPointerException

- if obj or m or args or any of the elements of args is null.

---

#### getMethodCallSyntax

String

getMethodCallSyntax​(

String

obj,

String

m,

String

... args)

Returns a String which can be used to invoke a method of a Java object using the syntax
of the supported scripting language. For instance, an implementation for a Javascript
engine might be;

```java
public String getMethodCallSyntax(String obj,
String m, String... args) {
String ret = obj;
ret += "." + m + "(";
for (int i = 0; i < args.length; i++) {
ret += args[i];
if (i < args.length - 1) {
ret += ",";
}
}
ret += ")";
return ret;
}
```

public String getMethodCallSyntax(String obj,
String m, String... args) {
String ret = obj;
ret += "." + m + "(";
for (int i = 0; i < args.length; i++) {
ret += args[i];
if (i < args.length - 1) {
ret += ",";
}
}
ret += ")";
return ret;
}

getOutputStatement

```java
String
getOutputStatement​(
String
toDisplay)
```

Returns a String that can be used as a statement to display the specified String using
the syntax of the supported scripting language. For instance, the implementation for a Perl
engine might be;

```java
public String getOutputStatement(String toDisplay) {
return "print(" + toDisplay + ")";
}
```

**Parameters:** toDisplay

- The String to be displayed by the returned statement.
**Returns:** The string used to display the String in the syntax of the scripting language.

---

#### getOutputStatement

String

getOutputStatement​(

String

toDisplay)

Returns a String that can be used as a statement to display the specified String using
the syntax of the supported scripting language. For instance, the implementation for a Perl
engine might be;

```java
public String getOutputStatement(String toDisplay) {
return "print(" + toDisplay + ")";
}
```

public String getOutputStatement(String toDisplay) {
return "print(" + toDisplay + ")";
}

getProgram

```java
String
getProgram​(
String
... statements)
```

Returns a valid scripting language executable program with given statements.
For instance an implementation for a PHP engine might be:

```java
public String getProgram(String... statements) {
String retval = "<?\n";
int len = statements.length;
for (int i = 0; i < len; i++) {
retval += statements[i] + ";\n";
}
return retval += "?>";
}
```

**Parameters:** statements

- The statements to be executed. May be return values of
calls to the

getMethodCallSyntax

and

getOutputStatement

methods.
**Returns:** The Program
**Throws:** NullPointerException

- if the

statements

array or any of its elements is null

---

#### getProgram

String

getProgram​(

String

... statements)

Returns a valid scripting language executable program with given statements.
For instance an implementation for a PHP engine might be:

```java
public String getProgram(String... statements) {
String retval = "<?\n";
int len = statements.length;
for (int i = 0; i < len; i++) {
retval += statements[i] + ";\n";
}
return retval += "?>";
}
```

public String getProgram(String... statements) {
String retval = "<?\n";
int len = statements.length;
for (int i = 0; i < len; i++) {
retval += statements[i] + ";\n";
}
return retval += "?>";
}

getScriptEngine

```java
ScriptEngine
getScriptEngine()
```

Returns an instance of the

ScriptEngine

associated with this

ScriptEngineFactory

. A new ScriptEngine is generally
returned, but implementations may pool, share or reuse engines.

**Returns:** A new

ScriptEngine

instance.

---

#### getScriptEngine

ScriptEngine

getScriptEngine()

Returns an instance of the

ScriptEngine

associated with this

ScriptEngineFactory

. A new ScriptEngine is generally
returned, but implementations may pool, share or reuse engines.

---

