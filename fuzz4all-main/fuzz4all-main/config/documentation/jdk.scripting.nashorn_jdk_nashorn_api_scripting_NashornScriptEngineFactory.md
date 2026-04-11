# Class NashornScriptEngineFactory

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\scripting\NashornScriptEngineFactory.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
NashornScriptEngineFactory

extends
Object

implements
ScriptEngineFactory
```

JSR-223 compliant script engine factory for Nashorn. The engine answers for:

- names

"nashorn"

,

"Nashorn"

,

"js"

,

"JS"

,

"JavaScript"

,

"javascript"

,

"ECMAScript"

, and

"ecmascript"

;
- MIME types

"application/javascript"

,

"application/ecmascript"

,

"text/javascript"

, and

"text/ecmascript"

;
- as well as for the extension

"js"

.

Programs executing in engines created using

getScriptEngine(String[])

will have the passed arguments
accessible as a global variable named

"arguments"

.

**All Implemented Interfaces:** ScriptEngineFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public NashornScriptEngineFactory()

*No description found.*

---

### Method Details

#### public
ScriptEngine
getScriptEngine​(
ClassLoader
appLoader)

Create a new Script engine initialized with the given class loader.

**Parameters:**
- appLoader

- class loader to be used as script "app" class loader.

**Returns:**
- newly created script engine.

**Throws:**
- SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### public
ScriptEngine
getScriptEngine​(
ClassFilter
classFilter)

Create a new Script engine initialized with the given class filter.

**Parameters:**
- classFilter

- class filter to use.

**Returns:**
- newly created script engine.

**Throws:**
- NullPointerException

- if

classFilter

is

null
- SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### public
ScriptEngine
getScriptEngine​(
String
... args)

Create a new Script engine initialized with the given arguments.

**Parameters:**
- args

- arguments array passed to script engine.

**Returns:**
- newly created script engine.

**Throws:**
- NullPointerException

- if

args

is

null
- SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### public
ScriptEngine
getScriptEngine​(
String
[] args,

ClassLoader
appLoader)

Create a new Script engine initialized with the given arguments and the given class loader.

**Parameters:**
- args

- arguments array passed to script engine.
- appLoader

- class loader to be used as script "app" class loader.

**Returns:**
- newly created script engine.

**Throws:**
- NullPointerException

- if

args

is

null
- SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### public
ScriptEngine
getScriptEngine​(
String
[] args,

ClassLoader
appLoader,

ClassFilter
classFilter)

Create a new Script engine initialized with the given arguments, class loader and class filter.

**Parameters:**
- args

- arguments array passed to script engine.
- appLoader

- class loader to be used as script "app" class loader.
- classFilter

- class filter to use.

**Returns:**
- newly created script engine.

**Throws:**
- NullPointerException

- if

args

or

classFilter

is

null
- SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

### Additional Sections

#### Class NashornScriptEngineFactory

java.lang.Object

- jdk.nashorn.api.scripting.NashornScriptEngineFactory

jdk.nashorn.api.scripting.NashornScriptEngineFactory

**All Implemented Interfaces:** ScriptEngineFactory

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
NashornScriptEngineFactory

extends
Object

implements
ScriptEngineFactory
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

JSR-223 compliant script engine factory for Nashorn. The engine answers for:

- names

"nashorn"

,

"Nashorn"

,

"js"

,

"JS"

,

"JavaScript"

,

"javascript"

,

"ECMAScript"

, and

"ecmascript"

;
- MIME types

"application/javascript"

,

"application/ecmascript"

,

"text/javascript"

, and

"text/ecmascript"

;
- as well as for the extension

"js"

.

Programs executing in engines created using

getScriptEngine(String[])

will have the passed arguments
accessible as a global variable named

"arguments"

.

**Since:** 1.8u40

@Deprecated

(

since

="11",

forRemoval

=true)
public final class

NashornScriptEngineFactory

extends

Object

implements

ScriptEngineFactory

JSR-223 compliant script engine factory for Nashorn. The engine answers for:

- names

"nashorn"

,

"Nashorn"

,

"js"

,

"JS"

,

"JavaScript"

,

"javascript"

,

"ECMAScript"

, and

"ecmascript"

;
- MIME types

"application/javascript"

,

"application/ecmascript"

,

"text/javascript"

, and

"text/ecmascript"

;
- as well as for the extension

"js"

.

Programs executing in engines created using

getScriptEngine(String[])

will have the passed arguments
accessible as a global variable named

"arguments"

.

names

"nashorn"

,

"Nashorn"

,

"js"

,

"JS"

,

"JavaScript"

,

"javascript"

,

"ECMAScript"

, and

"ecmascript"

;

MIME types

"application/javascript"

,

"application/ecmascript"

,

"text/javascript"

, and

"text/ecmascript"

;

as well as for the extension

"js"

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NashornScriptEngineFactory

()

Deprecated, for removal: This API element is subject to removal in a future version.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

ScriptEngine

getScriptEngine

​(

ClassLoader

appLoader)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class loader.

ScriptEngine

getScriptEngine

​(

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments.

ScriptEngine

getScriptEngine

​(

String

[] args,

ClassLoader

appLoader)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments and the given class loader.

ScriptEngine

getScriptEngine

​(

String

[] args,

ClassLoader

appLoader,

ClassFilter

classFilter)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments, class loader and class filter.

ScriptEngine

getScriptEngine

​(

ClassFilter

classFilter)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class filter.

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

ScriptEngineFactory

getEngineName

,

getEngineVersion

,

getExtensions

,

getLanguageName

,

getLanguageVersion

,

getMethodCallSyntax

,

getMimeTypes

,

getNames

,

getOutputStatement

,

getParameter

,

getProgram

,

getScriptEngine

Constructor Summary

Constructors

Constructor

Description

NashornScriptEngineFactory

()

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

ScriptEngine

getScriptEngine

​(

ClassLoader

appLoader)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class loader.

ScriptEngine

getScriptEngine

​(

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments.

ScriptEngine

getScriptEngine

​(

String

[] args,

ClassLoader

appLoader)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments and the given class loader.

ScriptEngine

getScriptEngine

​(

String

[] args,

ClassLoader

appLoader,

ClassFilter

classFilter)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments, class loader and class filter.

ScriptEngine

getScriptEngine

​(

ClassFilter

classFilter)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class filter.

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

ScriptEngineFactory

getEngineName

,

getEngineVersion

,

getExtensions

,

getLanguageName

,

getLanguageVersion

,

getMethodCallSyntax

,

getMimeTypes

,

getNames

,

getOutputStatement

,

getParameter

,

getProgram

,

getScriptEngine

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class loader.

Create a new Script engine initialized with the given arguments.

Create a new Script engine initialized with the given arguments and the given class loader.

Create a new Script engine initialized with the given arguments, class loader and class filter.

Create a new Script engine initialized with the given class filter.

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

ScriptEngineFactory

getEngineName

,

getEngineVersion

,

getExtensions

,

getLanguageName

,

getLanguageVersion

,

getMethodCallSyntax

,

getMimeTypes

,

getNames

,

getOutputStatement

,

getParameter

,

getProgram

,

getScriptEngine

---

#### Methods declared in interface javax.script. ScriptEngineFactory

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NashornScriptEngineFactory

```java
public NashornScriptEngineFactory()
```

Deprecated, for removal: This API element is subject to removal in a future version.

============ METHOD DETAIL ==========

- Method Detail

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
ClassLoader
appLoader)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class loader.

**Parameters:** appLoader

- class loader to be used as script "app" class loader.
**Returns:** newly created script engine.
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
ClassFilter
classFilter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class filter.

**Parameters:** classFilter

- class filter to use.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

classFilter

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments.

**Parameters:** args

- arguments array passed to script engine.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

args

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
String
[] args,

ClassLoader
appLoader)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments and the given class loader.

**Parameters:** args

- arguments array passed to script engine.
**Parameters:** appLoader

- class loader to be used as script "app" class loader.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

args

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
String
[] args,

ClassLoader
appLoader,

ClassFilter
classFilter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments, class loader and class filter.

**Parameters:** args

- arguments array passed to script engine.
**Parameters:** appLoader

- class loader to be used as script "app" class loader.
**Parameters:** classFilter

- class filter to use.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

args

or

classFilter

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

Constructor Detail

- NashornScriptEngineFactory

```java
public NashornScriptEngineFactory()
```

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### Constructor Detail

NashornScriptEngineFactory

```java
public NashornScriptEngineFactory()
```

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### NashornScriptEngineFactory

public NashornScriptEngineFactory()

Method Detail

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
ClassLoader
appLoader)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class loader.

**Parameters:** appLoader

- class loader to be used as script "app" class loader.
**Returns:** newly created script engine.
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
ClassFilter
classFilter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class filter.

**Parameters:** classFilter

- class filter to use.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

classFilter

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments.

**Parameters:** args

- arguments array passed to script engine.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

args

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
String
[] args,

ClassLoader
appLoader)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments and the given class loader.

**Parameters:** args

- arguments array passed to script engine.
**Parameters:** appLoader

- class loader to be used as script "app" class loader.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

args

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

- getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
String
[] args,

ClassLoader
appLoader,

ClassFilter
classFilter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments, class loader and class filter.

**Parameters:** args

- arguments array passed to script engine.
**Parameters:** appLoader

- class loader to be used as script "app" class loader.
**Parameters:** classFilter

- class filter to use.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

args

or

classFilter

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### Method Detail

getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
ClassLoader
appLoader)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class loader.

**Parameters:** appLoader

- class loader to be used as script "app" class loader.
**Returns:** newly created script engine.
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### getScriptEngine

public

ScriptEngine

getScriptEngine​(

ClassLoader

appLoader)

Create a new Script engine initialized with the given class loader.

getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
ClassFilter
classFilter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given class filter.

**Parameters:** classFilter

- class filter to use.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

classFilter

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### getScriptEngine

public

ScriptEngine

getScriptEngine​(

ClassFilter

classFilter)

Create a new Script engine initialized with the given class filter.

getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments.

**Parameters:** args

- arguments array passed to script engine.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

args

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### getScriptEngine

public

ScriptEngine

getScriptEngine​(

String

... args)

Create a new Script engine initialized with the given arguments.

getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
String
[] args,

ClassLoader
appLoader)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments and the given class loader.

**Parameters:** args

- arguments array passed to script engine.
**Parameters:** appLoader

- class loader to be used as script "app" class loader.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

args

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### getScriptEngine

public

ScriptEngine

getScriptEngine​(

String

[] args,

ClassLoader

appLoader)

Create a new Script engine initialized with the given arguments and the given class loader.

getScriptEngine

```java
public
ScriptEngine
getScriptEngine​(
String
[] args,

ClassLoader
appLoader,

ClassFilter
classFilter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a new Script engine initialized with the given arguments, class loader and class filter.

**Parameters:** args

- arguments array passed to script engine.
**Parameters:** appLoader

- class loader to be used as script "app" class loader.
**Parameters:** classFilter

- class filter to use.
**Returns:** newly created script engine.
**Throws:** NullPointerException

- if

args

or

classFilter

is

null
**Throws:** SecurityException

- if the security manager's

checkPermission

denies

RuntimePermission("nashorn.setConfig")

---

#### getScriptEngine

public

ScriptEngine

getScriptEngine​(

String

[] args,

ClassLoader

appLoader,

ClassFilter

classFilter)

Create a new Script engine initialized with the given arguments, class loader and class filter.

---

