# Class SimpleScriptContext

**Source:** `java.scripting\javax\script\SimpleScriptContext.html`

### Class Description

```java
public class
SimpleScriptContext

extends
Object

implements
ScriptContext
```

Simple implementation of ScriptContext.

**All Implemented Interfaces:** ScriptContext

---

### Field Details

#### protected
Writer
writer

This is the writer to be used to output from scripts.
By default, a

PrintWriter

based on

System.out

is used. Accessor methods getWriter, setWriter are used to manage
this field.

**See Also:**
- System.out

,

PrintWriter

---

#### protected
Writer
errorWriter

This is the writer to be used to output errors from scripts.
By default, a

PrintWriter

based on

System.err

is
used. Accessor methods getErrorWriter, setErrorWriter are used to manage
this field.

**See Also:**
- System.err

,

PrintWriter

---

#### protected
Reader
reader

This is the reader to be used for input from scripts.
By default, a

InputStreamReader

based on

System.in

is used and default charset is used by this reader. Accessor methods
getReader, setReader are used to manage this field.

**See Also:**
- System.in

,

InputStreamReader

---

#### protected
Bindings
engineScope

This is the engine scope bindings.
By default, a

SimpleBindings

is used. Accessor
methods setBindings, getBindings are used to manage this field.

**See Also:**
- SimpleBindings

---

#### protected
Bindings
globalScope

This is the global scope bindings.
By default, a null value (which means no global scope) is used. Accessor
methods setBindings, getBindings are used to manage this field.

---

### Constructor Details

#### public SimpleScriptContext()

Create a

SimpleScriptContext

.

---

### Method Details

#### public void setBindings​(
Bindings
bindings,
int scope)

Sets a

Bindings

of attributes for the given scope. If the value
of scope is

ENGINE_SCOPE

the given

Bindings

replaces the

engineScope

field. If the value
of scope is

GLOBAL_SCOPE

the given

Bindings

replaces the

globalScope

field.

**Specified by:**
- setBindings

in interface

ScriptContext

**Parameters:**
- bindings

- The

Bindings

of attributes to set.
- scope

- The value of the scope in which the attributes are set.

**Throws:**
- IllegalArgumentException

- if scope is invalid.
- NullPointerException

- if the value of scope is

ENGINE_SCOPE

and
the specified

Bindings

is null.

---

#### public
Object
getAttribute​(
String
name)

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

**Specified by:**
- getAttribute

in interface

ScriptContext

**Parameters:**
- name

- The name of the attribute to retrieve.

**Returns:**
- The value of the attribute in the lowest scope for
which an attribute with the given name is defined. Returns
null if no attribute with the name exists in any scope.

**Throws:**
- NullPointerException

- if the name is null.
- IllegalArgumentException

- if the name is empty.

---

#### public
Object
getAttribute​(
String
name,
int scope)

Gets the value of an attribute in a given scope.

**Specified by:**
- getAttribute

in interface

ScriptContext

**Parameters:**
- name

- The name of the attribute to retrieve.
- scope

- The scope in which to retrieve the attribute.

**Returns:**
- The value of the attribute. Returns

null

is the name
does not exist in the given scope.

**Throws:**
- IllegalArgumentException

- if the name is empty or if the value of scope is invalid.
- NullPointerException

- if the name is null.

---

#### public
Object
removeAttribute​(
String
name,
int scope)

Remove an attribute in a given scope.

**Specified by:**
- removeAttribute

in interface

ScriptContext

**Parameters:**
- name

- The name of the attribute to remove
- scope

- The scope in which to remove the attribute

**Returns:**
- The removed value.

**Throws:**
- IllegalArgumentException

- if the name is empty or if the scope is invalid.
- NullPointerException

- if the name is null.

---

#### public void setAttribute​(
String
name,

Object
value,
int scope)

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

**Specified by:**
- setAttribute

in interface

ScriptContext

**Parameters:**
- name

- The name of the attribute to set
- value

- The value of the attribute
- scope

- The scope in which to set the attribute

**Throws:**
- IllegalArgumentException

- if the name is empty or if the scope is invalid.
- NullPointerException

- if the name is null.

---

#### public int getAttributesScope​(
String
name)

Get the lowest scope in which an attribute is defined.

**Specified by:**
- getAttributesScope

in interface

ScriptContext

**Parameters:**
- name

- Name of the attribute
.

**Returns:**
- The lowest scope. Returns -1 if no attribute with the given
name is defined in any scope.

**Throws:**
- NullPointerException

- if name is null.
- IllegalArgumentException

- if name is empty.

---

#### public
Bindings
getBindings​(int scope)

Returns the value of the

engineScope

field if specified scope is

ENGINE_SCOPE

. Returns the value of the

globalScope

field if the specified scope is

GLOBAL_SCOPE

.

**Specified by:**
- getBindings

in interface

ScriptContext

**Parameters:**
- scope

- The specified scope

**Returns:**
- The value of either the

engineScope

or

globalScope

field.

**Throws:**
- IllegalArgumentException

- if the value of scope is invalid.

---

### Additional Sections

#### Class SimpleScriptContext

java.lang.Object

- javax.script.SimpleScriptContext

javax.script.SimpleScriptContext

**All Implemented Interfaces:** ScriptContext

```java
public class
SimpleScriptContext

extends
Object

implements
ScriptContext
```

Simple implementation of ScriptContext.

**Since:** 1.6

public class

SimpleScriptContext

extends

Object

implements

ScriptContext

Simple implementation of ScriptContext.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Bindings

engineScope

This is the engine scope bindings.

protected

Writer

errorWriter

This is the writer to be used to output errors from scripts.

protected

Bindings

globalScope

This is the global scope bindings.

protected

Reader

reader

This is the reader to be used for input from scripts.

protected

Writer

writer

This is the writer to be used to output from scripts.

- Fields declared in interface javax.script.

ScriptContext

ENGINE_SCOPE

,

GLOBAL_SCOPE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleScriptContext

()

Create a

SimpleScriptContext

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getAttribute

​(

String

name)

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order.

Object

getAttribute

​(

String

name,
int scope)

Gets the value of an attribute in a given scope.

int

getAttributesScope

​(

String

name)

Get the lowest scope in which an attribute is defined.

Bindings

getBindings

​(int scope)

Returns the value of the

engineScope

field if specified scope is

ENGINE_SCOPE

.

Object

removeAttribute

​(

String

name,
int scope)

Remove an attribute in a given scope.

void

setAttribute

​(

String

name,

Object

value,
int scope)

Sets the value of an attribute in a given scope.

void

setBindings

​(

Bindings

bindings,
int scope)

Sets a

Bindings

of attributes for the given scope.

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

ScriptContext

getErrorWriter

,

getReader

,

getScopes

,

getWriter

,

setErrorWriter

,

setReader

,

setWriter

Field Summary

Fields

Modifier and Type

Field

Description

protected

Bindings

engineScope

This is the engine scope bindings.

protected

Writer

errorWriter

This is the writer to be used to output errors from scripts.

protected

Bindings

globalScope

This is the global scope bindings.

protected

Reader

reader

This is the reader to be used for input from scripts.

protected

Writer

writer

This is the writer to be used to output from scripts.

- Fields declared in interface javax.script.

ScriptContext

ENGINE_SCOPE

,

GLOBAL_SCOPE

---

#### Field Summary

This is the engine scope bindings.

This is the writer to be used to output errors from scripts.

This is the global scope bindings.

This is the reader to be used for input from scripts.

This is the writer to be used to output from scripts.

Fields declared in interface javax.script.

ScriptContext

ENGINE_SCOPE

,

GLOBAL_SCOPE

---

#### Fields declared in interface javax.script. ScriptContext

Constructor Summary

Constructors

Constructor

Description

SimpleScriptContext

()

Create a

SimpleScriptContext

.

---

#### Constructor Summary

Create a

SimpleScriptContext

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getAttribute

​(

String

name)

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order.

Object

getAttribute

​(

String

name,
int scope)

Gets the value of an attribute in a given scope.

int

getAttributesScope

​(

String

name)

Get the lowest scope in which an attribute is defined.

Bindings

getBindings

​(int scope)

Returns the value of the

engineScope

field if specified scope is

ENGINE_SCOPE

.

Object

removeAttribute

​(

String

name,
int scope)

Remove an attribute in a given scope.

void

setAttribute

​(

String

name,

Object

value,
int scope)

Sets the value of an attribute in a given scope.

void

setBindings

​(

Bindings

bindings,
int scope)

Sets a

Bindings

of attributes for the given scope.

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

ScriptContext

getErrorWriter

,

getReader

,

getScopes

,

getWriter

,

setErrorWriter

,

setReader

,

setWriter

---

#### Method Summary

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order.

Gets the value of an attribute in a given scope.

Get the lowest scope in which an attribute is defined.

Returns the value of the

engineScope

field if specified scope is

ENGINE_SCOPE

.

Remove an attribute in a given scope.

Sets the value of an attribute in a given scope.

Sets a

Bindings

of attributes for the given scope.

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

ScriptContext

getErrorWriter

,

getReader

,

getScopes

,

getWriter

,

setErrorWriter

,

setReader

,

setWriter

---

#### Methods declared in interface javax.script. ScriptContext

============ FIELD DETAIL ===========

- Field Detail

- writer

```java
protected
Writer
writer
```

This is the writer to be used to output from scripts.
By default, a

PrintWriter

based on

System.out

is used. Accessor methods getWriter, setWriter are used to manage
this field.

**See Also:** System.out

,

PrintWriter

- errorWriter

```java
protected
Writer
errorWriter
```

This is the writer to be used to output errors from scripts.
By default, a

PrintWriter

based on

System.err

is
used. Accessor methods getErrorWriter, setErrorWriter are used to manage
this field.

**See Also:** System.err

,

PrintWriter

- reader

```java
protected
Reader
reader
```

This is the reader to be used for input from scripts.
By default, a

InputStreamReader

based on

System.in

is used and default charset is used by this reader. Accessor methods
getReader, setReader are used to manage this field.

**See Also:** System.in

,

InputStreamReader

- engineScope

```java
protected
Bindings
engineScope
```

This is the engine scope bindings.
By default, a

SimpleBindings

is used. Accessor
methods setBindings, getBindings are used to manage this field.

**See Also:** SimpleBindings

- globalScope

```java
protected
Bindings
globalScope
```

This is the global scope bindings.
By default, a null value (which means no global scope) is used. Accessor
methods setBindings, getBindings are used to manage this field.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleScriptContext

```java
public SimpleScriptContext()
```

Create a

SimpleScriptContext

.

============ METHOD DETAIL ==========

- Method Detail

- setBindings

```java
public void setBindings​(
Bindings
bindings,
int scope)
```

Sets a

Bindings

of attributes for the given scope. If the value
of scope is

ENGINE_SCOPE

the given

Bindings

replaces the

engineScope

field. If the value
of scope is

GLOBAL_SCOPE

the given

Bindings

replaces the

globalScope

field.

**Specified by:** setBindings

in interface

ScriptContext
**Parameters:** bindings

- The

Bindings

of attributes to set.
**Parameters:** scope

- The value of the scope in which the attributes are set.
**Throws:** IllegalArgumentException

- if scope is invalid.
**Throws:** NullPointerException

- if the value of scope is

ENGINE_SCOPE

and
the specified

Bindings

is null.

- getAttribute

```java
public
Object
getAttribute​(
String
name)
```

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

**Specified by:** getAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to retrieve.
**Returns:** The value of the attribute in the lowest scope for
which an attribute with the given name is defined. Returns
null if no attribute with the name exists in any scope.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty.

- getAttribute

```java
public
Object
getAttribute​(
String
name,
int scope)
```

Gets the value of an attribute in a given scope.

**Specified by:** getAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to retrieve.
**Parameters:** scope

- The scope in which to retrieve the attribute.
**Returns:** The value of the attribute. Returns

null

is the name
does not exist in the given scope.
**Throws:** IllegalArgumentException

- if the name is empty or if the value of scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- removeAttribute

```java
public
Object
removeAttribute​(
String
name,
int scope)
```

Remove an attribute in a given scope.

**Specified by:** removeAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to remove
**Parameters:** scope

- The scope in which to remove the attribute
**Returns:** The removed value.
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- setAttribute

```java
public void setAttribute​(
String
name,

Object
value,
int scope)
```

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

**Specified by:** setAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to set
**Parameters:** value

- The value of the attribute
**Parameters:** scope

- The scope in which to set the attribute
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- getAttributesScope

```java
public int getAttributesScope​(
String
name)
```

Get the lowest scope in which an attribute is defined.

**Specified by:** getAttributesScope

in interface

ScriptContext
**Parameters:** name

- Name of the attribute
.
**Returns:** The lowest scope. Returns -1 if no attribute with the given
name is defined in any scope.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if name is empty.

- getBindings

```java
public
Bindings
getBindings​(int scope)
```

Returns the value of the

engineScope

field if specified scope is

ENGINE_SCOPE

. Returns the value of the

globalScope

field if the specified scope is

GLOBAL_SCOPE

.

**Specified by:** getBindings

in interface

ScriptContext
**Parameters:** scope

- The specified scope
**Returns:** The value of either the

engineScope

or

globalScope

field.
**Throws:** IllegalArgumentException

- if the value of scope is invalid.

Field Detail

- writer

```java
protected
Writer
writer
```

This is the writer to be used to output from scripts.
By default, a

PrintWriter

based on

System.out

is used. Accessor methods getWriter, setWriter are used to manage
this field.

**See Also:** System.out

,

PrintWriter

- errorWriter

```java
protected
Writer
errorWriter
```

This is the writer to be used to output errors from scripts.
By default, a

PrintWriter

based on

System.err

is
used. Accessor methods getErrorWriter, setErrorWriter are used to manage
this field.

**See Also:** System.err

,

PrintWriter

- reader

```java
protected
Reader
reader
```

This is the reader to be used for input from scripts.
By default, a

InputStreamReader

based on

System.in

is used and default charset is used by this reader. Accessor methods
getReader, setReader are used to manage this field.

**See Also:** System.in

,

InputStreamReader

- engineScope

```java
protected
Bindings
engineScope
```

This is the engine scope bindings.
By default, a

SimpleBindings

is used. Accessor
methods setBindings, getBindings are used to manage this field.

**See Also:** SimpleBindings

- globalScope

```java
protected
Bindings
globalScope
```

This is the global scope bindings.
By default, a null value (which means no global scope) is used. Accessor
methods setBindings, getBindings are used to manage this field.

---

#### Field Detail

writer

```java
protected
Writer
writer
```

This is the writer to be used to output from scripts.
By default, a

PrintWriter

based on

System.out

is used. Accessor methods getWriter, setWriter are used to manage
this field.

**See Also:** System.out

,

PrintWriter

---

#### writer

protected

Writer

writer

This is the writer to be used to output from scripts.
By default, a

PrintWriter

based on

System.out

is used. Accessor methods getWriter, setWriter are used to manage
this field.

errorWriter

```java
protected
Writer
errorWriter
```

This is the writer to be used to output errors from scripts.
By default, a

PrintWriter

based on

System.err

is
used. Accessor methods getErrorWriter, setErrorWriter are used to manage
this field.

**See Also:** System.err

,

PrintWriter

---

#### errorWriter

protected

Writer

errorWriter

This is the writer to be used to output errors from scripts.
By default, a

PrintWriter

based on

System.err

is
used. Accessor methods getErrorWriter, setErrorWriter are used to manage
this field.

reader

```java
protected
Reader
reader
```

This is the reader to be used for input from scripts.
By default, a

InputStreamReader

based on

System.in

is used and default charset is used by this reader. Accessor methods
getReader, setReader are used to manage this field.

**See Also:** System.in

,

InputStreamReader

---

#### reader

protected

Reader

reader

This is the reader to be used for input from scripts.
By default, a

InputStreamReader

based on

System.in

is used and default charset is used by this reader. Accessor methods
getReader, setReader are used to manage this field.

engineScope

```java
protected
Bindings
engineScope
```

This is the engine scope bindings.
By default, a

SimpleBindings

is used. Accessor
methods setBindings, getBindings are used to manage this field.

**See Also:** SimpleBindings

---

#### engineScope

protected

Bindings

engineScope

This is the engine scope bindings.
By default, a

SimpleBindings

is used. Accessor
methods setBindings, getBindings are used to manage this field.

globalScope

```java
protected
Bindings
globalScope
```

This is the global scope bindings.
By default, a null value (which means no global scope) is used. Accessor
methods setBindings, getBindings are used to manage this field.

---

#### globalScope

protected

Bindings

globalScope

This is the global scope bindings.
By default, a null value (which means no global scope) is used. Accessor
methods setBindings, getBindings are used to manage this field.

Constructor Detail

- SimpleScriptContext

```java
public SimpleScriptContext()
```

Create a

SimpleScriptContext

.

---

#### Constructor Detail

SimpleScriptContext

```java
public SimpleScriptContext()
```

Create a

SimpleScriptContext

.

---

#### SimpleScriptContext

public SimpleScriptContext()

Create a

SimpleScriptContext

.

Method Detail

- setBindings

```java
public void setBindings​(
Bindings
bindings,
int scope)
```

Sets a

Bindings

of attributes for the given scope. If the value
of scope is

ENGINE_SCOPE

the given

Bindings

replaces the

engineScope

field. If the value
of scope is

GLOBAL_SCOPE

the given

Bindings

replaces the

globalScope

field.

**Specified by:** setBindings

in interface

ScriptContext
**Parameters:** bindings

- The

Bindings

of attributes to set.
**Parameters:** scope

- The value of the scope in which the attributes are set.
**Throws:** IllegalArgumentException

- if scope is invalid.
**Throws:** NullPointerException

- if the value of scope is

ENGINE_SCOPE

and
the specified

Bindings

is null.

- getAttribute

```java
public
Object
getAttribute​(
String
name)
```

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

**Specified by:** getAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to retrieve.
**Returns:** The value of the attribute in the lowest scope for
which an attribute with the given name is defined. Returns
null if no attribute with the name exists in any scope.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty.

- getAttribute

```java
public
Object
getAttribute​(
String
name,
int scope)
```

Gets the value of an attribute in a given scope.

**Specified by:** getAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to retrieve.
**Parameters:** scope

- The scope in which to retrieve the attribute.
**Returns:** The value of the attribute. Returns

null

is the name
does not exist in the given scope.
**Throws:** IllegalArgumentException

- if the name is empty or if the value of scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- removeAttribute

```java
public
Object
removeAttribute​(
String
name,
int scope)
```

Remove an attribute in a given scope.

**Specified by:** removeAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to remove
**Parameters:** scope

- The scope in which to remove the attribute
**Returns:** The removed value.
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- setAttribute

```java
public void setAttribute​(
String
name,

Object
value,
int scope)
```

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

**Specified by:** setAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to set
**Parameters:** value

- The value of the attribute
**Parameters:** scope

- The scope in which to set the attribute
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- getAttributesScope

```java
public int getAttributesScope​(
String
name)
```

Get the lowest scope in which an attribute is defined.

**Specified by:** getAttributesScope

in interface

ScriptContext
**Parameters:** name

- Name of the attribute
.
**Returns:** The lowest scope. Returns -1 if no attribute with the given
name is defined in any scope.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if name is empty.

- getBindings

```java
public
Bindings
getBindings​(int scope)
```

Returns the value of the

engineScope

field if specified scope is

ENGINE_SCOPE

. Returns the value of the

globalScope

field if the specified scope is

GLOBAL_SCOPE

.

**Specified by:** getBindings

in interface

ScriptContext
**Parameters:** scope

- The specified scope
**Returns:** The value of either the

engineScope

or

globalScope

field.
**Throws:** IllegalArgumentException

- if the value of scope is invalid.

---

#### Method Detail

setBindings

```java
public void setBindings​(
Bindings
bindings,
int scope)
```

Sets a

Bindings

of attributes for the given scope. If the value
of scope is

ENGINE_SCOPE

the given

Bindings

replaces the

engineScope

field. If the value
of scope is

GLOBAL_SCOPE

the given

Bindings

replaces the

globalScope

field.

**Specified by:** setBindings

in interface

ScriptContext
**Parameters:** bindings

- The

Bindings

of attributes to set.
**Parameters:** scope

- The value of the scope in which the attributes are set.
**Throws:** IllegalArgumentException

- if scope is invalid.
**Throws:** NullPointerException

- if the value of scope is

ENGINE_SCOPE

and
the specified

Bindings

is null.

---

#### setBindings

public void setBindings​(

Bindings

bindings,
int scope)

Sets a

Bindings

of attributes for the given scope. If the value
of scope is

ENGINE_SCOPE

the given

Bindings

replaces the

engineScope

field. If the value
of scope is

GLOBAL_SCOPE

the given

Bindings

replaces the

globalScope

field.

getAttribute

```java
public
Object
getAttribute​(
String
name)
```

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

**Specified by:** getAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to retrieve.
**Returns:** The value of the attribute in the lowest scope for
which an attribute with the given name is defined. Returns
null if no attribute with the name exists in any scope.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty.

---

#### getAttribute

public

Object

getAttribute​(

String

name)

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

getAttribute

```java
public
Object
getAttribute​(
String
name,
int scope)
```

Gets the value of an attribute in a given scope.

**Specified by:** getAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to retrieve.
**Parameters:** scope

- The scope in which to retrieve the attribute.
**Returns:** The value of the attribute. Returns

null

is the name
does not exist in the given scope.
**Throws:** IllegalArgumentException

- if the name is empty or if the value of scope is invalid.
**Throws:** NullPointerException

- if the name is null.

---

#### getAttribute

public

Object

getAttribute​(

String

name,
int scope)

Gets the value of an attribute in a given scope.

removeAttribute

```java
public
Object
removeAttribute​(
String
name,
int scope)
```

Remove an attribute in a given scope.

**Specified by:** removeAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to remove
**Parameters:** scope

- The scope in which to remove the attribute
**Returns:** The removed value.
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

---

#### removeAttribute

public

Object

removeAttribute​(

String

name,
int scope)

Remove an attribute in a given scope.

setAttribute

```java
public void setAttribute​(
String
name,

Object
value,
int scope)
```

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

**Specified by:** setAttribute

in interface

ScriptContext
**Parameters:** name

- The name of the attribute to set
**Parameters:** value

- The value of the attribute
**Parameters:** scope

- The scope in which to set the attribute
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

---

#### setAttribute

public void setAttribute​(

String

name,

Object

value,
int scope)

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

getAttributesScope

```java
public int getAttributesScope​(
String
name)
```

Get the lowest scope in which an attribute is defined.

**Specified by:** getAttributesScope

in interface

ScriptContext
**Parameters:** name

- Name of the attribute
.
**Returns:** The lowest scope. Returns -1 if no attribute with the given
name is defined in any scope.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if name is empty.

---

#### getAttributesScope

public int getAttributesScope​(

String

name)

Get the lowest scope in which an attribute is defined.

getBindings

```java
public
Bindings
getBindings​(int scope)
```

Returns the value of the

engineScope

field if specified scope is

ENGINE_SCOPE

. Returns the value of the

globalScope

field if the specified scope is

GLOBAL_SCOPE

.

**Specified by:** getBindings

in interface

ScriptContext
**Parameters:** scope

- The specified scope
**Returns:** The value of either the

engineScope

or

globalScope

field.
**Throws:** IllegalArgumentException

- if the value of scope is invalid.

---

#### getBindings

public

Bindings

getBindings​(int scope)

Returns the value of the

engineScope

field if specified scope is

ENGINE_SCOPE

. Returns the value of the

globalScope

field if the specified scope is

GLOBAL_SCOPE

.

---

