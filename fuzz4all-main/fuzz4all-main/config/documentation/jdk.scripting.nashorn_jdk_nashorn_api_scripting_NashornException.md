# Class NashornException

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\scripting\NashornException.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public abstract class
NashornException

extends
RuntimeException
```

This is base exception for all Nashorn exceptions. These originate from
user's ECMAScript code. Example: script parse errors, exceptions thrown from
scripts. Note that ScriptEngine methods like "eval", "invokeMethod",
"invokeFunction" will wrap this as ScriptException and throw it. But, there
are cases where user may need to access this exception (or implementation
defined subtype of this). For example, if java interface is implemented by a
script object or Java access to script object properties via java.util.Map
interface. In these cases, user code will get an instance of this or
implementation defined subclass.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected NashornException​(
String
msg,

String
fileName,
int line,
int column)

Constructor to initialize error message, file name, line and column numbers.

**Parameters:**
- msg

- exception message
- fileName

- file name
- line

- line number
- column

- column number

---

#### protected NashornException​(
String
msg,

Throwable
cause,

String
fileName,
int line,
int column)

Constructor to initialize error message, cause exception, file name, line and column numbers.

**Parameters:**
- msg

- exception message
- cause

- exception cause
- fileName

- file name
- line

- line number
- column

- column number

---

#### protected NashornException​(
String
msg,

Throwable
cause)

Constructor to initialize error message and cause exception.

**Parameters:**
- msg

- exception message
- cause

- exception cause

---

### Method Details

#### public final
String
getFileName()

Get the source file name for this

NashornException

**Returns:**
- the file name

---

#### public final void setFileName​(
String
fileName)

Set the source file name for this

NashornException

**Parameters:**
- fileName

- the file name

---

#### public final int getLineNumber()

Get the line number for this

NashornException

**Returns:**
- the line number

---

#### public final void setLineNumber​(int line)

Set the line number for this

NashornException

**Parameters:**
- line

- the line number

---

#### public final int getColumnNumber()

Get the column for this

NashornException

**Returns:**
- the column number

---

#### public final void setColumnNumber​(int column)

Set the column for this

NashornException

**Parameters:**
- column

- the column number

---

#### public static
StackTraceElement
[] getScriptFrames​(
Throwable
exception)

Returns array javascript stack frames from the given exception object.

**Parameters:**
- exception

- exception from which stack frames are retrieved and filtered

**Returns:**
- array of javascript stack frames

---

#### public static
String
getScriptStackString​(
Throwable
exception)

Return a formatted script stack trace string with frames information separated by '\n'

**Parameters:**
- exception

- exception for which script stack string is returned

**Returns:**
- formatted stack trace string

---

#### protected
Object
getThrown()

Get the thrown object. Subclass responsibility

**Returns:**
- thrown object

---

#### public
Object
getEcmaError()

Return the underlying ECMA error object, if available.

**Returns:**
- underlying ECMA Error object's mirror or whatever was thrown
from script such as a String, Number or a Boolean.

---

#### public void setEcmaError​(
Object
ecmaError)

Return the underlying ECMA error object, if available.

**Parameters:**
- ecmaError

- underlying ECMA Error object's mirror or whatever was thrown
from script such as a String, Number or a Boolean.

---

### Additional Sections

#### Class NashornException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - jdk.nashorn.api.scripting.NashornException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - jdk.nashorn.api.scripting.NashornException

java.lang.Exception

- java.lang.RuntimeException
- - jdk.nashorn.api.scripting.NashornException

java.lang.RuntimeException

- jdk.nashorn.api.scripting.NashornException

jdk.nashorn.api.scripting.NashornException

**All Implemented Interfaces:** Serializable

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public abstract class
NashornException

extends
RuntimeException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

This is base exception for all Nashorn exceptions. These originate from
user's ECMAScript code. Example: script parse errors, exceptions thrown from
scripts. Note that ScriptEngine methods like "eval", "invokeMethod",
"invokeFunction" will wrap this as ScriptException and throw it. But, there
are cases where user may need to access this exception (or implementation
defined subtype of this). For example, if java interface is implemented by a
script object or Java access to script object properties via java.util.Map
interface. In these cases, user code will get an instance of this or
implementation defined subclass.

**Since:** 1.8u40
**See Also:** Serialized Form

@Deprecated

(

since

="11",

forRemoval

=true)
public abstract class

NashornException

extends

RuntimeException

This is base exception for all Nashorn exceptions. These originate from
user's ECMAScript code. Example: script parse errors, exceptions thrown from
scripts. Note that ScriptEngine methods like "eval", "invokeMethod",
"invokeFunction" will wrap this as ScriptException and throw it. But, there
are cases where user may need to access this exception (or implementation
defined subtype of this). For example, if java interface is implemented by a
script object or Java access to script object properties via java.util.Map
interface. In these cases, user code will get an instance of this or
implementation defined subclass.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

NashornException

​(

String

msg,

String

fileName,
int line,
int column)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, file name, line and column numbers.

protected

NashornException

​(

String

msg,

Throwable

cause)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message and cause exception.

protected

NashornException

​(

String

msg,

Throwable

cause,

String

fileName,
int line,
int column)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, cause exception, file name, line and column numbers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the column for this

NashornException

Object

getEcmaError

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

String

getFileName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the source file name for this

NashornException

int

getLineNumber

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the line number for this

NashornException

static

StackTraceElement

[]

getScriptFrames

​(

Throwable

exception)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns array javascript stack frames from the given exception object.

static

String

getScriptStackString

​(

Throwable

exception)

Deprecated, for removal: This API element is subject to removal in a future version.

Return a formatted script stack trace string with frames information separated by '\n'

protected

Object

getThrown

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the thrown object.

void

setColumnNumber

​(int column)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the column for this

NashornException

void

setEcmaError

​(

Object

ecmaError)

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

void

setFileName

​(

String

fileName)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the source file name for this

NashornException

void

setLineNumber

​(int line)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the line number for this

NashornException

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

NashornException

​(

String

msg,

String

fileName,
int line,
int column)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, file name, line and column numbers.

protected

NashornException

​(

String

msg,

Throwable

cause)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message and cause exception.

protected

NashornException

​(

String

msg,

Throwable

cause,

String

fileName,
int line,
int column)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, cause exception, file name, line and column numbers.

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, file name, line and column numbers.

Constructor to initialize error message and cause exception.

Constructor to initialize error message, cause exception, file name, line and column numbers.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the column for this

NashornException

Object

getEcmaError

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

String

getFileName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the source file name for this

NashornException

int

getLineNumber

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the line number for this

NashornException

static

StackTraceElement

[]

getScriptFrames

​(

Throwable

exception)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns array javascript stack frames from the given exception object.

static

String

getScriptStackString

​(

Throwable

exception)

Deprecated, for removal: This API element is subject to removal in a future version.

Return a formatted script stack trace string with frames information separated by '\n'

protected

Object

getThrown

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the thrown object.

void

setColumnNumber

​(int column)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the column for this

NashornException

void

setEcmaError

​(

Object

ecmaError)

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

void

setFileName

​(

String

fileName)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the source file name for this

NashornException

void

setLineNumber

​(int line)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the line number for this

NashornException

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Get the column for this

NashornException

Return the underlying ECMA error object, if available.

Get the source file name for this

NashornException

Get the line number for this

NashornException

Returns array javascript stack frames from the given exception object.

Return a formatted script stack trace string with frames information separated by '\n'

Get the thrown object.

Set the column for this

NashornException

Set the source file name for this

NashornException

Set the line number for this

NashornException

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NashornException

```java
protected NashornException​(
String
msg,

String
fileName,
int line,
int column)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, file name, line and column numbers.

**Parameters:** msg

- exception message
**Parameters:** fileName

- file name
**Parameters:** line

- line number
**Parameters:** column

- column number

- NashornException

```java
protected NashornException​(
String
msg,

Throwable
cause,

String
fileName,
int line,
int column)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, cause exception, file name, line and column numbers.

**Parameters:** msg

- exception message
**Parameters:** cause

- exception cause
**Parameters:** fileName

- file name
**Parameters:** line

- line number
**Parameters:** column

- column number

- NashornException

```java
protected NashornException​(
String
msg,

Throwable
cause)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message and cause exception.

**Parameters:** msg

- exception message
**Parameters:** cause

- exception cause

============ METHOD DETAIL ==========

- Method Detail

- getFileName

```java
public final
String
getFileName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the source file name for this

NashornException

**Returns:** the file name

- setFileName

```java
public final void setFileName​(
String
fileName)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the source file name for this

NashornException

**Parameters:** fileName

- the file name

- getLineNumber

```java
public final int getLineNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the line number for this

NashornException

**Returns:** the line number

- setLineNumber

```java
public final void setLineNumber​(int line)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the line number for this

NashornException

**Parameters:** line

- the line number

- getColumnNumber

```java
public final int getColumnNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the column for this

NashornException

**Returns:** the column number

- setColumnNumber

```java
public final void setColumnNumber​(int column)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the column for this

NashornException

**Parameters:** column

- the column number

- getScriptFrames

```java
public static
StackTraceElement
[] getScriptFrames​(
Throwable
exception)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns array javascript stack frames from the given exception object.

**Parameters:** exception

- exception from which stack frames are retrieved and filtered
**Returns:** array of javascript stack frames

- getScriptStackString

```java
public static
String
getScriptStackString​(
Throwable
exception)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a formatted script stack trace string with frames information separated by '\n'

**Parameters:** exception

- exception for which script stack string is returned
**Returns:** formatted stack trace string

- getThrown

```java
protected
Object
getThrown()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the thrown object. Subclass responsibility

**Returns:** thrown object

- getEcmaError

```java
public
Object
getEcmaError()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

**Returns:** underlying ECMA Error object's mirror or whatever was thrown
from script such as a String, Number or a Boolean.

- setEcmaError

```java
public void setEcmaError​(
Object
ecmaError)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

**Parameters:** ecmaError

- underlying ECMA Error object's mirror or whatever was thrown
from script such as a String, Number or a Boolean.

Constructor Detail

- NashornException

```java
protected NashornException​(
String
msg,

String
fileName,
int line,
int column)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, file name, line and column numbers.

**Parameters:** msg

- exception message
**Parameters:** fileName

- file name
**Parameters:** line

- line number
**Parameters:** column

- column number

- NashornException

```java
protected NashornException​(
String
msg,

Throwable
cause,

String
fileName,
int line,
int column)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, cause exception, file name, line and column numbers.

**Parameters:** msg

- exception message
**Parameters:** cause

- exception cause
**Parameters:** fileName

- file name
**Parameters:** line

- line number
**Parameters:** column

- column number

- NashornException

```java
protected NashornException​(
String
msg,

Throwable
cause)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message and cause exception.

**Parameters:** msg

- exception message
**Parameters:** cause

- exception cause

---

#### Constructor Detail

NashornException

```java
protected NashornException​(
String
msg,

String
fileName,
int line,
int column)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, file name, line and column numbers.

**Parameters:** msg

- exception message
**Parameters:** fileName

- file name
**Parameters:** line

- line number
**Parameters:** column

- column number

---

#### NashornException

protected NashornException​(

String

msg,

String

fileName,
int line,
int column)

Constructor to initialize error message, file name, line and column numbers.

NashornException

```java
protected NashornException​(
String
msg,

Throwable
cause,

String
fileName,
int line,
int column)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message, cause exception, file name, line and column numbers.

**Parameters:** msg

- exception message
**Parameters:** cause

- exception cause
**Parameters:** fileName

- file name
**Parameters:** line

- line number
**Parameters:** column

- column number

---

#### NashornException

protected NashornException​(

String

msg,

Throwable

cause,

String

fileName,
int line,
int column)

Constructor to initialize error message, cause exception, file name, line and column numbers.

NashornException

```java
protected NashornException​(
String
msg,

Throwable
cause)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor to initialize error message and cause exception.

**Parameters:** msg

- exception message
**Parameters:** cause

- exception cause

---

#### NashornException

protected NashornException​(

String

msg,

Throwable

cause)

Constructor to initialize error message and cause exception.

Method Detail

- getFileName

```java
public final
String
getFileName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the source file name for this

NashornException

**Returns:** the file name

- setFileName

```java
public final void setFileName​(
String
fileName)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the source file name for this

NashornException

**Parameters:** fileName

- the file name

- getLineNumber

```java
public final int getLineNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the line number for this

NashornException

**Returns:** the line number

- setLineNumber

```java
public final void setLineNumber​(int line)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the line number for this

NashornException

**Parameters:** line

- the line number

- getColumnNumber

```java
public final int getColumnNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the column for this

NashornException

**Returns:** the column number

- setColumnNumber

```java
public final void setColumnNumber​(int column)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the column for this

NashornException

**Parameters:** column

- the column number

- getScriptFrames

```java
public static
StackTraceElement
[] getScriptFrames​(
Throwable
exception)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns array javascript stack frames from the given exception object.

**Parameters:** exception

- exception from which stack frames are retrieved and filtered
**Returns:** array of javascript stack frames

- getScriptStackString

```java
public static
String
getScriptStackString​(
Throwable
exception)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a formatted script stack trace string with frames information separated by '\n'

**Parameters:** exception

- exception for which script stack string is returned
**Returns:** formatted stack trace string

- getThrown

```java
protected
Object
getThrown()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the thrown object. Subclass responsibility

**Returns:** thrown object

- getEcmaError

```java
public
Object
getEcmaError()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

**Returns:** underlying ECMA Error object's mirror or whatever was thrown
from script such as a String, Number or a Boolean.

- setEcmaError

```java
public void setEcmaError​(
Object
ecmaError)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

**Parameters:** ecmaError

- underlying ECMA Error object's mirror or whatever was thrown
from script such as a String, Number or a Boolean.

---

#### Method Detail

getFileName

```java
public final
String
getFileName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the source file name for this

NashornException

**Returns:** the file name

---

#### getFileName

public final

String

getFileName()

Get the source file name for this

NashornException

setFileName

```java
public final void setFileName​(
String
fileName)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the source file name for this

NashornException

**Parameters:** fileName

- the file name

---

#### setFileName

public final void setFileName​(

String

fileName)

Set the source file name for this

NashornException

getLineNumber

```java
public final int getLineNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the line number for this

NashornException

**Returns:** the line number

---

#### getLineNumber

public final int getLineNumber()

Get the line number for this

NashornException

setLineNumber

```java
public final void setLineNumber​(int line)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the line number for this

NashornException

**Parameters:** line

- the line number

---

#### setLineNumber

public final void setLineNumber​(int line)

Set the line number for this

NashornException

getColumnNumber

```java
public final int getColumnNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the column for this

NashornException

**Returns:** the column number

---

#### getColumnNumber

public final int getColumnNumber()

Get the column for this

NashornException

setColumnNumber

```java
public final void setColumnNumber​(int column)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the column for this

NashornException

**Parameters:** column

- the column number

---

#### setColumnNumber

public final void setColumnNumber​(int column)

Set the column for this

NashornException

getScriptFrames

```java
public static
StackTraceElement
[] getScriptFrames​(
Throwable
exception)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns array javascript stack frames from the given exception object.

**Parameters:** exception

- exception from which stack frames are retrieved and filtered
**Returns:** array of javascript stack frames

---

#### getScriptFrames

public static

StackTraceElement

[] getScriptFrames​(

Throwable

exception)

Returns array javascript stack frames from the given exception object.

getScriptStackString

```java
public static
String
getScriptStackString​(
Throwable
exception)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a formatted script stack trace string with frames information separated by '\n'

**Parameters:** exception

- exception for which script stack string is returned
**Returns:** formatted stack trace string

---

#### getScriptStackString

public static

String

getScriptStackString​(

Throwable

exception)

Return a formatted script stack trace string with frames information separated by '\n'

getThrown

```java
protected
Object
getThrown()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the thrown object. Subclass responsibility

**Returns:** thrown object

---

#### getThrown

protected

Object

getThrown()

Get the thrown object. Subclass responsibility

getEcmaError

```java
public
Object
getEcmaError()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

**Returns:** underlying ECMA Error object's mirror or whatever was thrown
from script such as a String, Number or a Boolean.

---

#### getEcmaError

public

Object

getEcmaError()

Return the underlying ECMA error object, if available.

setEcmaError

```java
public void setEcmaError​(
Object
ecmaError)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the underlying ECMA error object, if available.

**Parameters:** ecmaError

- underlying ECMA Error object's mirror or whatever was thrown
from script such as a String, Number or a Boolean.

---

#### setEcmaError

public void setEcmaError​(

Object

ecmaError)

Return the underlying ECMA error object, if available.

---

