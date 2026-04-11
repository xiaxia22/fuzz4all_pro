# Class ScriptUtils

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\scripting\ScriptUtils.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
ScriptUtils

extends
Object
```

Utilities that are to be called from script code.

**Since:** 1.8u40

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
String
parse​(
String
code,

String
name,
boolean includeLoc)

Returns AST as JSON compatible string. This is used to
implement "parse" function in resources/parse.js script.

**Parameters:**
- code

- code to be parsed
- name

- name of the code source (used for location)
- includeLoc

- tells whether to include location information for nodes or not

**Returns:**
- JSON string representation of AST of the supplied code

---

#### public static
String
format​(
String
format,

Object
[] args)

Method which converts javascript types to java types for the
String.format method (jrunscript function sprintf).

**Parameters:**
- format

- a format string
- args

- arguments referenced by the format specifiers in format

**Returns:**
- a formatted string

---

#### public static
Object
makeSynchronizedFunction​(
Object
func,

Object
sync)

Create a wrapper function that calls

func

synchronized on

sync

or, if that is undefined,

self

. Used to implement "sync" function in resources/mozilla_compat.js.

**Parameters:**
- func

- the function to wrap
- sync

- the object to synchronize on

**Returns:**
- a synchronizing wrapper function

**Throws:**
- IllegalArgumentException

- if func does not represent a script function

---

#### public static
ScriptObjectMirror
wrap​(
Object
obj)

Make a script object mirror on given object if needed.

**Parameters:**
- obj

- object to be wrapped

**Returns:**
- wrapped object

**Throws:**
- IllegalArgumentException

- if obj cannot be wrapped

---

#### public static
Object
unwrap​(
Object
obj)

Unwrap a script object mirror if needed.

**Parameters:**
- obj

- object to be unwrapped

**Returns:**
- unwrapped object

---

#### public static
Object
[] wrapArray​(
Object
[] args)

Wrap an array of object to script object mirrors if needed.

**Parameters:**
- args

- array to be unwrapped

**Returns:**
- wrapped array

---

#### public static
Object
[] unwrapArray​(
Object
[] args)

Unwrap an array of script object mirrors if needed.

**Parameters:**
- args

- array to be unwrapped

**Returns:**
- unwrapped array

---

#### public static
Object
convert​(
Object
obj,

Object
type)

Convert the given object to the given type.

**Parameters:**
- obj

- object to be converted
- type

- destination type to convert to. type is either a Class
or nashorn representation of a Java type returned by Java.type() call in script.

**Returns:**
- converted object

---

### Additional Sections

#### Class ScriptUtils

java.lang.Object

- jdk.nashorn.api.scripting.ScriptUtils

jdk.nashorn.api.scripting.ScriptUtils

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
ScriptUtils

extends
Object
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Utilities that are to be called from script code.

**Since:** 1.8u40

@Deprecated

(

since

="11",

forRemoval

=true)
public final class

ScriptUtils

extends

Object

Utilities that are to be called from script code.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Object

convert

​(

Object

obj,

Object

type)

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the given object to the given type.

static

String

format

​(

String

format,

Object

[] args)

Deprecated, for removal: This API element is subject to removal in a future version.

Method which converts javascript types to java types for the
String.format method (jrunscript function sprintf).

static

Object

makeSynchronizedFunction

​(

Object

func,

Object

sync)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a wrapper function that calls

func

synchronized on

sync

or, if that is undefined,

self

.

static

String

parse

​(

String

code,

String

name,
boolean includeLoc)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns AST as JSON compatible string.

static

Object

unwrap

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

static

Object

[]

unwrapArray

​(

Object

[] args)

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

static

ScriptObjectMirror

wrap

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

static

Object

[]

wrapArray

​(

Object

[] args)

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Object

convert

​(

Object

obj,

Object

type)

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the given object to the given type.

static

String

format

​(

String

format,

Object

[] args)

Deprecated, for removal: This API element is subject to removal in a future version.

Method which converts javascript types to java types for the
String.format method (jrunscript function sprintf).

static

Object

makeSynchronizedFunction

​(

Object

func,

Object

sync)

Deprecated, for removal: This API element is subject to removal in a future version.

Create a wrapper function that calls

func

synchronized on

sync

or, if that is undefined,

self

.

static

String

parse

​(

String

code,

String

name,
boolean includeLoc)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns AST as JSON compatible string.

static

Object

unwrap

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

static

Object

[]

unwrapArray

​(

Object

[] args)

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

static

ScriptObjectMirror

wrap

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

static

Object

[]

wrapArray

​(

Object

[] args)

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the given object to the given type.

Method which converts javascript types to java types for the
String.format method (jrunscript function sprintf).

Create a wrapper function that calls

func

synchronized on

sync

or, if that is undefined,

self

.

Returns AST as JSON compatible string.

Unwrap a script object mirror if needed.

Unwrap an array of script object mirrors if needed.

Make a script object mirror on given object if needed.

Wrap an array of object to script object mirrors if needed.

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

============ METHOD DETAIL ==========

- Method Detail

- parse

```java
public static
String
parse​(
String
code,

String
name,
boolean includeLoc)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns AST as JSON compatible string. This is used to
implement "parse" function in resources/parse.js script.

**Parameters:** code

- code to be parsed
**Parameters:** name

- name of the code source (used for location)
**Parameters:** includeLoc

- tells whether to include location information for nodes or not
**Returns:** JSON string representation of AST of the supplied code

- format

```java
public static
String
format​(
String
format,

Object
[] args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Method which converts javascript types to java types for the
String.format method (jrunscript function sprintf).

**Parameters:** format

- a format string
**Parameters:** args

- arguments referenced by the format specifiers in format
**Returns:** a formatted string

- makeSynchronizedFunction

```java
public static
Object
makeSynchronizedFunction​(
Object
func,

Object
sync)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a wrapper function that calls

func

synchronized on

sync

or, if that is undefined,

self

. Used to implement "sync" function in resources/mozilla_compat.js.

**Parameters:** func

- the function to wrap
**Parameters:** sync

- the object to synchronize on
**Returns:** a synchronizing wrapper function
**Throws:** IllegalArgumentException

- if func does not represent a script function

- wrap

```java
public static
ScriptObjectMirror
wrap​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

**Parameters:** obj

- object to be wrapped
**Returns:** wrapped object
**Throws:** IllegalArgumentException

- if obj cannot be wrapped

- unwrap

```java
public static
Object
unwrap​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

**Parameters:** obj

- object to be unwrapped
**Returns:** unwrapped object

- wrapArray

```java
public static
Object
[] wrapArray​(
Object
[] args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Returns:** wrapped array

- unwrapArray

```java
public static
Object
[] unwrapArray​(
Object
[] args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Returns:** unwrapped array

- convert

```java
public static
Object
convert​(
Object
obj,

Object
type)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the given object to the given type.

**Parameters:** obj

- object to be converted
**Parameters:** type

- destination type to convert to. type is either a Class
or nashorn representation of a Java type returned by Java.type() call in script.
**Returns:** converted object

Method Detail

- parse

```java
public static
String
parse​(
String
code,

String
name,
boolean includeLoc)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns AST as JSON compatible string. This is used to
implement "parse" function in resources/parse.js script.

**Parameters:** code

- code to be parsed
**Parameters:** name

- name of the code source (used for location)
**Parameters:** includeLoc

- tells whether to include location information for nodes or not
**Returns:** JSON string representation of AST of the supplied code

- format

```java
public static
String
format​(
String
format,

Object
[] args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Method which converts javascript types to java types for the
String.format method (jrunscript function sprintf).

**Parameters:** format

- a format string
**Parameters:** args

- arguments referenced by the format specifiers in format
**Returns:** a formatted string

- makeSynchronizedFunction

```java
public static
Object
makeSynchronizedFunction​(
Object
func,

Object
sync)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a wrapper function that calls

func

synchronized on

sync

or, if that is undefined,

self

. Used to implement "sync" function in resources/mozilla_compat.js.

**Parameters:** func

- the function to wrap
**Parameters:** sync

- the object to synchronize on
**Returns:** a synchronizing wrapper function
**Throws:** IllegalArgumentException

- if func does not represent a script function

- wrap

```java
public static
ScriptObjectMirror
wrap​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

**Parameters:** obj

- object to be wrapped
**Returns:** wrapped object
**Throws:** IllegalArgumentException

- if obj cannot be wrapped

- unwrap

```java
public static
Object
unwrap​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

**Parameters:** obj

- object to be unwrapped
**Returns:** unwrapped object

- wrapArray

```java
public static
Object
[] wrapArray​(
Object
[] args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Returns:** wrapped array

- unwrapArray

```java
public static
Object
[] unwrapArray​(
Object
[] args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Returns:** unwrapped array

- convert

```java
public static
Object
convert​(
Object
obj,

Object
type)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the given object to the given type.

**Parameters:** obj

- object to be converted
**Parameters:** type

- destination type to convert to. type is either a Class
or nashorn representation of a Java type returned by Java.type() call in script.
**Returns:** converted object

---

#### Method Detail

parse

```java
public static
String
parse​(
String
code,

String
name,
boolean includeLoc)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns AST as JSON compatible string. This is used to
implement "parse" function in resources/parse.js script.

**Parameters:** code

- code to be parsed
**Parameters:** name

- name of the code source (used for location)
**Parameters:** includeLoc

- tells whether to include location information for nodes or not
**Returns:** JSON string representation of AST of the supplied code

---

#### parse

public static

String

parse​(

String

code,

String

name,
boolean includeLoc)

Returns AST as JSON compatible string. This is used to
implement "parse" function in resources/parse.js script.

format

```java
public static
String
format​(
String
format,

Object
[] args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Method which converts javascript types to java types for the
String.format method (jrunscript function sprintf).

**Parameters:** format

- a format string
**Parameters:** args

- arguments referenced by the format specifiers in format
**Returns:** a formatted string

---

#### format

public static

String

format​(

String

format,

Object

[] args)

Method which converts javascript types to java types for the
String.format method (jrunscript function sprintf).

makeSynchronizedFunction

```java
public static
Object
makeSynchronizedFunction​(
Object
func,

Object
sync)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Create a wrapper function that calls

func

synchronized on

sync

or, if that is undefined,

self

. Used to implement "sync" function in resources/mozilla_compat.js.

**Parameters:** func

- the function to wrap
**Parameters:** sync

- the object to synchronize on
**Returns:** a synchronizing wrapper function
**Throws:** IllegalArgumentException

- if func does not represent a script function

---

#### makeSynchronizedFunction

public static

Object

makeSynchronizedFunction​(

Object

func,

Object

sync)

Create a wrapper function that calls

func

synchronized on

sync

or, if that is undefined,

self

. Used to implement "sync" function in resources/mozilla_compat.js.

wrap

```java
public static
ScriptObjectMirror
wrap​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

**Parameters:** obj

- object to be wrapped
**Returns:** wrapped object
**Throws:** IllegalArgumentException

- if obj cannot be wrapped

---

#### wrap

public static

ScriptObjectMirror

wrap​(

Object

obj)

Make a script object mirror on given object if needed.

unwrap

```java
public static
Object
unwrap​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

**Parameters:** obj

- object to be unwrapped
**Returns:** unwrapped object

---

#### unwrap

public static

Object

unwrap​(

Object

obj)

Unwrap a script object mirror if needed.

wrapArray

```java
public static
Object
[] wrapArray​(
Object
[] args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Returns:** wrapped array

---

#### wrapArray

public static

Object

[] wrapArray​(

Object

[] args)

Wrap an array of object to script object mirrors if needed.

unwrapArray

```java
public static
Object
[] unwrapArray​(
Object
[] args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Returns:** unwrapped array

---

#### unwrapArray

public static

Object

[] unwrapArray​(

Object

[] args)

Unwrap an array of script object mirrors if needed.

convert

```java
public static
Object
convert​(
Object
obj,

Object
type)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the given object to the given type.

**Parameters:** obj

- object to be converted
**Parameters:** type

- destination type to convert to. type is either a Class
or nashorn representation of a Java type returned by Java.type() call in script.
**Returns:** converted object

---

#### convert

public static

Object

convert​(

Object

obj,

Object

type)

Convert the given object to the given type.

---

