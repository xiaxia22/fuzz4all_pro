# Class SettingDescriptorInfo

**Source:** `jdk.management.jfr\jdk\management\jfr\SettingDescriptorInfo.html`

### Class Description

```java
public final class
SettingDescriptorInfo

extends
Object
```

Management class that describes a setting, for example name, description and
default value.

**Since:** 9
**See Also:** EventType.getSettingDescriptors()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getLabel()

Returns the human-readable name of the setting associated with this

SettingDescriptorInfo

(for example,

"Threshold"

).

**Returns:**
- the label for this setting, not

null

---

#### public
String
getName()

Returns the name of the setting associated with this

SettingDescriptorInfo

(for example,

"threshold"

).

**Returns:**
- the name of this setting, not

null

---

#### public
String
getDescription()

Returns the description of the setting associated this

SettingDescriptorInfo

(for example,

"The duration an event must exceed to be be recorded"

).

**Returns:**
- the description of this setting, not null

---

#### public
String
getTypeName()

Returns the type name of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.settings.Threshold"

).

The type can be used to identify what type of setting this is.

**Returns:**
- the name of this settings type, not

null

---

#### public
String
getContentType()

Returns the content type of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.jfr.Timespan"

).

The content type can be used to determine how the setting should be
rendered in a graphical user interface.

**Returns:**
- the name of this settings type, not

null

---

#### public
String
getDefaultValue()

Returns the default value of the setting associated this

SettingDescriptorInfo

(for example,

"20 ms"

).

**Returns:**
- default value for this setting, not

null

**See Also:**
- SettingDescriptor.getDefaultValue()

---

#### public static
SettingDescriptorInfo
from​(
CompositeData
cd)

Returns an

SettingDescriptorInfo

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

name

String

label

String

description

String

typeName

String

contentType

String

defaultValue

String

**Parameters:**
- cd

-

CompositeData

representing the

SettingDescriptorInfo

to
return

**Returns:**
- a

SettingDescriptorInfo

, or

null

if

cd

is

null

**Throws:**
- IllegalArgumentException

- if

cd

does not represent a valid

EventTypeInfo

---

#### public
String
toString()

Returns a

String

description of this

SettingDescriptorInfo

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string describing this setting, not

null

---

### Additional Sections

#### Class SettingDescriptorInfo

java.lang.Object

- jdk.management.jfr.SettingDescriptorInfo

jdk.management.jfr.SettingDescriptorInfo

```java
public final class
SettingDescriptorInfo

extends
Object
```

Management class that describes a setting, for example name, description and
default value.

**Since:** 9
**See Also:** EventType.getSettingDescriptors()

public final class

SettingDescriptorInfo

extends

Object

Management class that describes a setting, for example name, description and
default value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

SettingDescriptorInfo

from

​(

CompositeData

cd)

Returns an

SettingDescriptorInfo

represented by the specified

CompositeData

String

getContentType

()

Returns the content type of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.jfr.Timespan"

).

String

getDefaultValue

()

Returns the default value of the setting associated this

SettingDescriptorInfo

(for example,

"20 ms"

).

String

getDescription

()

Returns the description of the setting associated this

SettingDescriptorInfo

(for example,

"The duration an event must exceed to be be recorded"

).

String

getLabel

()

Returns the human-readable name of the setting associated with this

SettingDescriptorInfo

(for example,

"Threshold"

).

String

getName

()

Returns the name of the setting associated with this

SettingDescriptorInfo

(for example,

"threshold"

).

String

getTypeName

()

Returns the type name of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.settings.Threshold"

).

String

toString

()

Returns a

String

description of this

SettingDescriptorInfo

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

wait

,

wait

,

wait

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

SettingDescriptorInfo

from

​(

CompositeData

cd)

Returns an

SettingDescriptorInfo

represented by the specified

CompositeData

String

getContentType

()

Returns the content type of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.jfr.Timespan"

).

String

getDefaultValue

()

Returns the default value of the setting associated this

SettingDescriptorInfo

(for example,

"20 ms"

).

String

getDescription

()

Returns the description of the setting associated this

SettingDescriptorInfo

(for example,

"The duration an event must exceed to be be recorded"

).

String

getLabel

()

Returns the human-readable name of the setting associated with this

SettingDescriptorInfo

(for example,

"Threshold"

).

String

getName

()

Returns the name of the setting associated with this

SettingDescriptorInfo

(for example,

"threshold"

).

String

getTypeName

()

Returns the type name of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.settings.Threshold"

).

String

toString

()

Returns a

String

description of this

SettingDescriptorInfo

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

wait

,

wait

,

wait

---

#### Method Summary

Returns an

SettingDescriptorInfo

represented by the specified

CompositeData

Returns the content type of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.jfr.Timespan"

).

Returns the default value of the setting associated this

SettingDescriptorInfo

(for example,

"20 ms"

).

Returns the description of the setting associated this

SettingDescriptorInfo

(for example,

"The duration an event must exceed to be be recorded"

).

Returns the human-readable name of the setting associated with this

SettingDescriptorInfo

(for example,

"Threshold"

).

Returns the name of the setting associated with this

SettingDescriptorInfo

(for example,

"threshold"

).

Returns the type name of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.settings.Threshold"

).

Returns a

String

description of this

SettingDescriptorInfo

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- getLabel

```java
public
String
getLabel()
```

Returns the human-readable name of the setting associated with this

SettingDescriptorInfo

(for example,

"Threshold"

).

**Returns:** the label for this setting, not

null

- getName

```java
public
String
getName()
```

Returns the name of the setting associated with this

SettingDescriptorInfo

(for example,

"threshold"

).

**Returns:** the name of this setting, not

null

- getDescription

```java
public
String
getDescription()
```

Returns the description of the setting associated this

SettingDescriptorInfo

(for example,

"The duration an event must exceed to be be recorded"

).

**Returns:** the description of this setting, not null

- getTypeName

```java
public
String
getTypeName()
```

Returns the type name of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.settings.Threshold"

).

The type can be used to identify what type of setting this is.

**Returns:** the name of this settings type, not

null

- getContentType

```java
public
String
getContentType()
```

Returns the content type of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.jfr.Timespan"

).

The content type can be used to determine how the setting should be
rendered in a graphical user interface.

**Returns:** the name of this settings type, not

null

- getDefaultValue

```java
public
String
getDefaultValue()
```

Returns the default value of the setting associated this

SettingDescriptorInfo

(for example,

"20 ms"

).

**Returns:** default value for this setting, not

null
**See Also:** SettingDescriptor.getDefaultValue()

- from

```java
public static
SettingDescriptorInfo
from​(
CompositeData
cd)
```

Returns an

SettingDescriptorInfo

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

name

String

label

String

description

String

typeName

String

contentType

String

defaultValue

String

**Parameters:** cd

-

CompositeData

representing the

SettingDescriptorInfo

to
return
**Returns:** a

SettingDescriptorInfo

, or

null

if

cd

is

null
**Throws:** IllegalArgumentException

- if

cd

does not represent a valid

EventTypeInfo

- toString

```java
public
String
toString()
```

Returns a

String

description of this

SettingDescriptorInfo

.

**Overrides:** toString

in class

Object
**Returns:** a string describing this setting, not

null

Method Detail

- getLabel

```java
public
String
getLabel()
```

Returns the human-readable name of the setting associated with this

SettingDescriptorInfo

(for example,

"Threshold"

).

**Returns:** the label for this setting, not

null

- getName

```java
public
String
getName()
```

Returns the name of the setting associated with this

SettingDescriptorInfo

(for example,

"threshold"

).

**Returns:** the name of this setting, not

null

- getDescription

```java
public
String
getDescription()
```

Returns the description of the setting associated this

SettingDescriptorInfo

(for example,

"The duration an event must exceed to be be recorded"

).

**Returns:** the description of this setting, not null

- getTypeName

```java
public
String
getTypeName()
```

Returns the type name of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.settings.Threshold"

).

The type can be used to identify what type of setting this is.

**Returns:** the name of this settings type, not

null

- getContentType

```java
public
String
getContentType()
```

Returns the content type of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.jfr.Timespan"

).

The content type can be used to determine how the setting should be
rendered in a graphical user interface.

**Returns:** the name of this settings type, not

null

- getDefaultValue

```java
public
String
getDefaultValue()
```

Returns the default value of the setting associated this

SettingDescriptorInfo

(for example,

"20 ms"

).

**Returns:** default value for this setting, not

null
**See Also:** SettingDescriptor.getDefaultValue()

- from

```java
public static
SettingDescriptorInfo
from​(
CompositeData
cd)
```

Returns an

SettingDescriptorInfo

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

name

String

label

String

description

String

typeName

String

contentType

String

defaultValue

String

**Parameters:** cd

-

CompositeData

representing the

SettingDescriptorInfo

to
return
**Returns:** a

SettingDescriptorInfo

, or

null

if

cd

is

null
**Throws:** IllegalArgumentException

- if

cd

does not represent a valid

EventTypeInfo

- toString

```java
public
String
toString()
```

Returns a

String

description of this

SettingDescriptorInfo

.

**Overrides:** toString

in class

Object
**Returns:** a string describing this setting, not

null

---

#### Method Detail

getLabel

```java
public
String
getLabel()
```

Returns the human-readable name of the setting associated with this

SettingDescriptorInfo

(for example,

"Threshold"

).

**Returns:** the label for this setting, not

null

---

#### getLabel

public

String

getLabel()

Returns the human-readable name of the setting associated with this

SettingDescriptorInfo

(for example,

"Threshold"

).

getName

```java
public
String
getName()
```

Returns the name of the setting associated with this

SettingDescriptorInfo

(for example,

"threshold"

).

**Returns:** the name of this setting, not

null

---

#### getName

public

String

getName()

Returns the name of the setting associated with this

SettingDescriptorInfo

(for example,

"threshold"

).

getDescription

```java
public
String
getDescription()
```

Returns the description of the setting associated this

SettingDescriptorInfo

(for example,

"The duration an event must exceed to be be recorded"

).

**Returns:** the description of this setting, not null

---

#### getDescription

public

String

getDescription()

Returns the description of the setting associated this

SettingDescriptorInfo

(for example,

"The duration an event must exceed to be be recorded"

).

getTypeName

```java
public
String
getTypeName()
```

Returns the type name of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.settings.Threshold"

).

The type can be used to identify what type of setting this is.

**Returns:** the name of this settings type, not

null

---

#### getTypeName

public

String

getTypeName()

Returns the type name of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.settings.Threshold"

).

The type can be used to identify what type of setting this is.

The type can be used to identify what type of setting this is.

getContentType

```java
public
String
getContentType()
```

Returns the content type of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.jfr.Timespan"

).

The content type can be used to determine how the setting should be
rendered in a graphical user interface.

**Returns:** the name of this settings type, not

null

---

#### getContentType

public

String

getContentType()

Returns the content type of the setting associated this

SettingDescriptorInfo

(for example,

"jdk.jfr.Timespan"

).

The content type can be used to determine how the setting should be
rendered in a graphical user interface.

The content type can be used to determine how the setting should be
rendered in a graphical user interface.

getDefaultValue

```java
public
String
getDefaultValue()
```

Returns the default value of the setting associated this

SettingDescriptorInfo

(for example,

"20 ms"

).

**Returns:** default value for this setting, not

null
**See Also:** SettingDescriptor.getDefaultValue()

---

#### getDefaultValue

public

String

getDefaultValue()

Returns the default value of the setting associated this

SettingDescriptorInfo

(for example,

"20 ms"

).

from

```java
public static
SettingDescriptorInfo
from​(
CompositeData
cd)
```

Returns an

SettingDescriptorInfo

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

name

String

label

String

description

String

typeName

String

contentType

String

defaultValue

String

**Parameters:** cd

-

CompositeData

representing the

SettingDescriptorInfo

to
return
**Returns:** a

SettingDescriptorInfo

, or

null

if

cd

is

null
**Throws:** IllegalArgumentException

- if

cd

does not represent a valid

EventTypeInfo

---

#### from

public static

SettingDescriptorInfo

from​(

CompositeData

cd)

Returns an

SettingDescriptorInfo

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

name

String

label

String

description

String

typeName

String

contentType

String

defaultValue

String

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

name

String

label

String

description

String

typeName

String

contentType

String

defaultValue

String

toString

```java
public
String
toString()
```

Returns a

String

description of this

SettingDescriptorInfo

.

**Overrides:** toString

in class

Object
**Returns:** a string describing this setting, not

null

---

#### toString

public

String

toString()

Returns a

String

description of this

SettingDescriptorInfo

.

---

