# Class NashornScriptEngine

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\scripting\NashornScriptEngine.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
NashornScriptEngine

extends
AbstractScriptEngine

implements
Compilable
,
Invocable
```

JSR-223 compliant script engine for Nashorn. Instances are not created directly, but rather returned through

ScriptEngineFactory.getScriptEngine()

. Note that this engine implements the

Compilable

and

Invocable

interfaces, allowing for efficient precompilation and repeated execution of scripts.

**All Implemented Interfaces:** Compilable

,

Invocable

,

ScriptEngine

---

### Field Details

#### public static final
String
NASHORN_GLOBAL

Key used to associate Nashorn global object mirror with arbitrary Bindings instance.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Class NashornScriptEngine

java.lang.Object

- javax.script.AbstractScriptEngine
- - jdk.nashorn.api.scripting.NashornScriptEngine

javax.script.AbstractScriptEngine

- jdk.nashorn.api.scripting.NashornScriptEngine

jdk.nashorn.api.scripting.NashornScriptEngine

**All Implemented Interfaces:** Compilable

,

Invocable

,

ScriptEngine

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
NashornScriptEngine

extends
AbstractScriptEngine

implements
Compilable
,
Invocable
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

JSR-223 compliant script engine for Nashorn. Instances are not created directly, but rather returned through

ScriptEngineFactory.getScriptEngine()

. Note that this engine implements the

Compilable

and

Invocable

interfaces, allowing for efficient precompilation and repeated execution of scripts.

**Since:** 1.8u40
**See Also:** NashornScriptEngineFactory

@Deprecated

(

since

="11",

forRemoval

=true)
public final class

NashornScriptEngine

extends

AbstractScriptEngine

implements

Compilable

,

Invocable

JSR-223 compliant script engine for Nashorn. Instances are not created directly, but rather returned through

ScriptEngineFactory.getScriptEngine()

. Note that this engine implements the

Compilable

and

Invocable

interfaces, allowing for efficient precompilation and repeated execution of scripts.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

NASHORN_GLOBAL

Deprecated, for removal: This API element is subject to removal in a future version.

Key used to associate Nashorn global object mirror with arbitrary Bindings instance.

- Fields declared in class javax.script.

AbstractScriptEngine

context

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

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.script.

AbstractScriptEngine

eval

,

eval

,

eval

,

eval

,

get

,

getBindings

,

getContext

,

getScriptContext

,

put

,

setBindings

,

setContext

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

Compilable

compile

,

compile

- Methods declared in interface javax.script.

Invocable

getInterface

,

getInterface

,

invokeFunction

,

invokeMethod

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

static

String

NASHORN_GLOBAL

Deprecated, for removal: This API element is subject to removal in a future version.

Key used to associate Nashorn global object mirror with arbitrary Bindings instance.

- Fields declared in class javax.script.

AbstractScriptEngine

context

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

Deprecated, for removal: This API element is subject to removal in a future version.

Key used to associate Nashorn global object mirror with arbitrary Bindings instance.

Fields declared in class javax.script.

AbstractScriptEngine

context

---

#### Fields declared in class javax.script. AbstractScriptEngine

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

Method Summary

- Methods declared in class javax.script.

AbstractScriptEngine

eval

,

eval

,

eval

,

eval

,

get

,

getBindings

,

getContext

,

getScriptContext

,

put

,

setBindings

,

setContext

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

Compilable

compile

,

compile

- Methods declared in interface javax.script.

Invocable

getInterface

,

getInterface

,

invokeFunction

,

invokeMethod

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

Methods declared in class javax.script.

AbstractScriptEngine

eval

,

eval

,

eval

,

eval

,

get

,

getBindings

,

getContext

,

getScriptContext

,

put

,

setBindings

,

setContext

---

#### Methods declared in class javax.script. AbstractScriptEngine

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

Compilable

compile

,

compile

---

#### Methods declared in interface javax.script. Compilable

Methods declared in interface javax.script.

Invocable

getInterface

,

getInterface

,

invokeFunction

,

invokeMethod

---

#### Methods declared in interface javax.script. Invocable

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

- NASHORN_GLOBAL

```java
public static final
String
NASHORN_GLOBAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Key used to associate Nashorn global object mirror with arbitrary Bindings instance.

**See Also:** Constant Field Values

Field Detail

- NASHORN_GLOBAL

```java
public static final
String
NASHORN_GLOBAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Key used to associate Nashorn global object mirror with arbitrary Bindings instance.

**See Also:** Constant Field Values

---

#### Field Detail

NASHORN_GLOBAL

```java
public static final
String
NASHORN_GLOBAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Key used to associate Nashorn global object mirror with arbitrary Bindings instance.

**See Also:** Constant Field Values

---

#### NASHORN_GLOBAL

public static final

String

NASHORN_GLOBAL

Key used to associate Nashorn global object mirror with arbitrary Bindings instance.

---

