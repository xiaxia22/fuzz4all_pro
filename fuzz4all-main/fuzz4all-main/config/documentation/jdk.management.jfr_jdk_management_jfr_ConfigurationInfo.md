# Class ConfigurationInfo

**Source:** `jdk.management.jfr\jdk\management\jfr\ConfigurationInfo.html`

### Class Description

```java
public final class
ConfigurationInfo

extends
Object
```

Management representation of a

Configuration

.

**Since:** 9
**See Also:** Configuration

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getProvider()

Returns the provider of the configuration associated with this

ConfigurationInfo

(for example,

"OpenJDK"

).

**Returns:**
- the provider, or

null

if doesn't exist

**See Also:**
- Configuration.getProvider()

---

#### public
String
getContents()

Returns the textual representation of the configuration associated with
this

ConfigurationInfo

, typically the contents of the
configuration file that was used to create the configuration.

**Returns:**
- contents, or

null

if doesn't exist

**See Also:**
- Configuration.getContents()

---

#### public
Map
<
String
,​
String
> getSettings()

Returns the settings for the configuration associated with this

ConfigurationInfo

.

**Returns:**
- a

Map

with settings, not

null

**See Also:**
- Configuration.getSettings()

---

#### public
String
getLabel()

Returns the human-readable name (for example,

"Continuous"

or

"Profiling"

) for
the configuration associated with this

ConfigurationInfo

**Returns:**
- the label, or

null

if doesn't exist

**See Also:**
- Configuration.getLabel()

---

#### public
String
getName()

Returns the name of the configuration associated with this

ConfigurationInfo

(for example,

"default"

).

**Returns:**
- the name, or

null

if doesn't exist

**See Also:**
- Configuration.getLabel()

---

#### public
String
getDescription()

Returns a short sentence that describes the configuration associated with
this

ConfigurationInfo

(for example,

"Low
overhead configuration safe for continuous use in production
environments"

.

**Returns:**
- the description, or

null

if doesn't exist

---

#### public static
ConfigurationInfo
from​(
CompositeData
cd)

Returns a

ConfigurationInfo

object represented by the specified

CompositeData

.

The following table shows the required attributes that the specified

CompositeData

must contain.

Required names and types for CompositeData

Name

Type

name

String

label

String

description

String

provider

String

contents

String

settings

javax.management.openmbean.TabularData

with a

TabularType

with the keys

"key"

and

"value"

, both
of the

String

type

**Parameters:**
- cd

-

CompositeData

representing a

ConfigurationInfo

**Returns:**
- a

ConfigurationInfo

object represented by

cd

if

cd

is not

null

,

null

otherwise

**Throws:**
- IllegalArgumentException

- if

cd

does not represent a

ConfigurationInfo

with the required attributes

---

#### public
String
toString()

Returns a description of the configuration that is associated with this

ConfigurationInfo

.

**Overrides:**
- toString

in class

Object

**Returns:**
- the description of the configuration, not

null

---

### Additional Sections

#### Class ConfigurationInfo

java.lang.Object

- jdk.management.jfr.ConfigurationInfo

jdk.management.jfr.ConfigurationInfo

```java
public final class
ConfigurationInfo

extends
Object
```

Management representation of a

Configuration

.

**Since:** 9
**See Also:** Configuration

public final class

ConfigurationInfo

extends

Object

Management representation of a

Configuration

.

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

ConfigurationInfo

from

​(

CompositeData

cd)

Returns a

ConfigurationInfo

object represented by the specified

CompositeData

.

String

getContents

()

Returns the textual representation of the configuration associated with
this

ConfigurationInfo

, typically the contents of the
configuration file that was used to create the configuration.

String

getDescription

()

Returns a short sentence that describes the configuration associated with
this

ConfigurationInfo

(for example,

"Low
overhead configuration safe for continuous use in production
environments"

.

String

getLabel

()

Returns the human-readable name (for example,

"Continuous"

or

"Profiling"

) for
the configuration associated with this

ConfigurationInfo

String

getName

()

Returns the name of the configuration associated with this

ConfigurationInfo

(for example,

"default"

).

String

getProvider

()

Returns the provider of the configuration associated with this

ConfigurationInfo

(for example,

"OpenJDK"

).

Map

<

String

,​

String

>

getSettings

()

Returns the settings for the configuration associated with this

ConfigurationInfo

.

String

toString

()

Returns a description of the configuration that is associated with this

ConfigurationInfo

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

ConfigurationInfo

from

​(

CompositeData

cd)

Returns a

ConfigurationInfo

object represented by the specified

CompositeData

.

String

getContents

()

Returns the textual representation of the configuration associated with
this

ConfigurationInfo

, typically the contents of the
configuration file that was used to create the configuration.

String

getDescription

()

Returns a short sentence that describes the configuration associated with
this

ConfigurationInfo

(for example,

"Low
overhead configuration safe for continuous use in production
environments"

.

String

getLabel

()

Returns the human-readable name (for example,

"Continuous"

or

"Profiling"

) for
the configuration associated with this

ConfigurationInfo

String

getName

()

Returns the name of the configuration associated with this

ConfigurationInfo

(for example,

"default"

).

String

getProvider

()

Returns the provider of the configuration associated with this

ConfigurationInfo

(for example,

"OpenJDK"

).

Map

<

String

,​

String

>

getSettings

()

Returns the settings for the configuration associated with this

ConfigurationInfo

.

String

toString

()

Returns a description of the configuration that is associated with this

ConfigurationInfo

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

Returns a

ConfigurationInfo

object represented by the specified

CompositeData

.

Returns the textual representation of the configuration associated with
this

ConfigurationInfo

, typically the contents of the
configuration file that was used to create the configuration.

Returns a short sentence that describes the configuration associated with
this

ConfigurationInfo

(for example,

"Low
overhead configuration safe for continuous use in production
environments"

.

Returns the human-readable name (for example,

"Continuous"

or

"Profiling"

) for
the configuration associated with this

ConfigurationInfo

Returns the name of the configuration associated with this

ConfigurationInfo

(for example,

"default"

).

Returns the provider of the configuration associated with this

ConfigurationInfo

(for example,

"OpenJDK"

).

Returns the settings for the configuration associated with this

ConfigurationInfo

.

Returns a description of the configuration that is associated with this

ConfigurationInfo

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

- getProvider

```java
public
String
getProvider()
```

Returns the provider of the configuration associated with this

ConfigurationInfo

(for example,

"OpenJDK"

).

**Returns:** the provider, or

null

if doesn't exist
**See Also:** Configuration.getProvider()

- getContents

```java
public
String
getContents()
```

Returns the textual representation of the configuration associated with
this

ConfigurationInfo

, typically the contents of the
configuration file that was used to create the configuration.

**Returns:** contents, or

null

if doesn't exist
**See Also:** Configuration.getContents()

- getSettings

```java
public
Map
<
String
,​
String
> getSettings()
```

Returns the settings for the configuration associated with this

ConfigurationInfo

.

**Returns:** a

Map

with settings, not

null
**See Also:** Configuration.getSettings()

- getLabel

```java
public
String
getLabel()
```

Returns the human-readable name (for example,

"Continuous"

or

"Profiling"

) for
the configuration associated with this

ConfigurationInfo

**Returns:** the label, or

null

if doesn't exist
**See Also:** Configuration.getLabel()

- getName

```java
public
String
getName()
```

Returns the name of the configuration associated with this

ConfigurationInfo

(for example,

"default"

).

**Returns:** the name, or

null

if doesn't exist
**See Also:** Configuration.getLabel()

- getDescription

```java
public
String
getDescription()
```

Returns a short sentence that describes the configuration associated with
this

ConfigurationInfo

(for example,

"Low
overhead configuration safe for continuous use in production
environments"

.

**Returns:** the description, or

null

if doesn't exist

- from

```java
public static
ConfigurationInfo
from​(
CompositeData
cd)
```

Returns a

ConfigurationInfo

object represented by the specified

CompositeData

.

The following table shows the required attributes that the specified

CompositeData

must contain.

Required names and types for CompositeData

Name

Type

name

String

label

String

description

String

provider

String

contents

String

settings

javax.management.openmbean.TabularData

with a

TabularType

with the keys

"key"

and

"value"

, both
of the

String

type

**Parameters:** cd

-

CompositeData

representing a

ConfigurationInfo
**Returns:** a

ConfigurationInfo

object represented by

cd

if

cd

is not

null

,

null

otherwise
**Throws:** IllegalArgumentException

- if

cd

does not represent a

ConfigurationInfo

with the required attributes

- toString

```java
public
String
toString()
```

Returns a description of the configuration that is associated with this

ConfigurationInfo

.

**Overrides:** toString

in class

Object
**Returns:** the description of the configuration, not

null

Method Detail

- getProvider

```java
public
String
getProvider()
```

Returns the provider of the configuration associated with this

ConfigurationInfo

(for example,

"OpenJDK"

).

**Returns:** the provider, or

null

if doesn't exist
**See Also:** Configuration.getProvider()

- getContents

```java
public
String
getContents()
```

Returns the textual representation of the configuration associated with
this

ConfigurationInfo

, typically the contents of the
configuration file that was used to create the configuration.

**Returns:** contents, or

null

if doesn't exist
**See Also:** Configuration.getContents()

- getSettings

```java
public
Map
<
String
,​
String
> getSettings()
```

Returns the settings for the configuration associated with this

ConfigurationInfo

.

**Returns:** a

Map

with settings, not

null
**See Also:** Configuration.getSettings()

- getLabel

```java
public
String
getLabel()
```

Returns the human-readable name (for example,

"Continuous"

or

"Profiling"

) for
the configuration associated with this

ConfigurationInfo

**Returns:** the label, or

null

if doesn't exist
**See Also:** Configuration.getLabel()

- getName

```java
public
String
getName()
```

Returns the name of the configuration associated with this

ConfigurationInfo

(for example,

"default"

).

**Returns:** the name, or

null

if doesn't exist
**See Also:** Configuration.getLabel()

- getDescription

```java
public
String
getDescription()
```

Returns a short sentence that describes the configuration associated with
this

ConfigurationInfo

(for example,

"Low
overhead configuration safe for continuous use in production
environments"

.

**Returns:** the description, or

null

if doesn't exist

- from

```java
public static
ConfigurationInfo
from​(
CompositeData
cd)
```

Returns a

ConfigurationInfo

object represented by the specified

CompositeData

.

The following table shows the required attributes that the specified

CompositeData

must contain.

Required names and types for CompositeData

Name

Type

name

String

label

String

description

String

provider

String

contents

String

settings

javax.management.openmbean.TabularData

with a

TabularType

with the keys

"key"

and

"value"

, both
of the

String

type

**Parameters:** cd

-

CompositeData

representing a

ConfigurationInfo
**Returns:** a

ConfigurationInfo

object represented by

cd

if

cd

is not

null

,

null

otherwise
**Throws:** IllegalArgumentException

- if

cd

does not represent a

ConfigurationInfo

with the required attributes

- toString

```java
public
String
toString()
```

Returns a description of the configuration that is associated with this

ConfigurationInfo

.

**Overrides:** toString

in class

Object
**Returns:** the description of the configuration, not

null

---

#### Method Detail

getProvider

```java
public
String
getProvider()
```

Returns the provider of the configuration associated with this

ConfigurationInfo

(for example,

"OpenJDK"

).

**Returns:** the provider, or

null

if doesn't exist
**See Also:** Configuration.getProvider()

---

#### getProvider

public

String

getProvider()

Returns the provider of the configuration associated with this

ConfigurationInfo

(for example,

"OpenJDK"

).

getContents

```java
public
String
getContents()
```

Returns the textual representation of the configuration associated with
this

ConfigurationInfo

, typically the contents of the
configuration file that was used to create the configuration.

**Returns:** contents, or

null

if doesn't exist
**See Also:** Configuration.getContents()

---

#### getContents

public

String

getContents()

Returns the textual representation of the configuration associated with
this

ConfigurationInfo

, typically the contents of the
configuration file that was used to create the configuration.

getSettings

```java
public
Map
<
String
,​
String
> getSettings()
```

Returns the settings for the configuration associated with this

ConfigurationInfo

.

**Returns:** a

Map

with settings, not

null
**See Also:** Configuration.getSettings()

---

#### getSettings

public

Map

<

String

,​

String

> getSettings()

Returns the settings for the configuration associated with this

ConfigurationInfo

.

getLabel

```java
public
String
getLabel()
```

Returns the human-readable name (for example,

"Continuous"

or

"Profiling"

) for
the configuration associated with this

ConfigurationInfo

**Returns:** the label, or

null

if doesn't exist
**See Also:** Configuration.getLabel()

---

#### getLabel

public

String

getLabel()

Returns the human-readable name (for example,

"Continuous"

or

"Profiling"

) for
the configuration associated with this

ConfigurationInfo

getName

```java
public
String
getName()
```

Returns the name of the configuration associated with this

ConfigurationInfo

(for example,

"default"

).

**Returns:** the name, or

null

if doesn't exist
**See Also:** Configuration.getLabel()

---

#### getName

public

String

getName()

Returns the name of the configuration associated with this

ConfigurationInfo

(for example,

"default"

).

getDescription

```java
public
String
getDescription()
```

Returns a short sentence that describes the configuration associated with
this

ConfigurationInfo

(for example,

"Low
overhead configuration safe for continuous use in production
environments"

.

**Returns:** the description, or

null

if doesn't exist

---

#### getDescription

public

String

getDescription()

Returns a short sentence that describes the configuration associated with
this

ConfigurationInfo

(for example,

"Low
overhead configuration safe for continuous use in production
environments"

.

from

```java
public static
ConfigurationInfo
from​(
CompositeData
cd)
```

Returns a

ConfigurationInfo

object represented by the specified

CompositeData

.

The following table shows the required attributes that the specified

CompositeData

must contain.

Required names and types for CompositeData

Name

Type

name

String

label

String

description

String

provider

String

contents

String

settings

javax.management.openmbean.TabularData

with a

TabularType

with the keys

"key"

and

"value"

, both
of the

String

type

**Parameters:** cd

-

CompositeData

representing a

ConfigurationInfo
**Returns:** a

ConfigurationInfo

object represented by

cd

if

cd

is not

null

,

null

otherwise
**Throws:** IllegalArgumentException

- if

cd

does not represent a

ConfigurationInfo

with the required attributes

---

#### from

public static

ConfigurationInfo

from​(

CompositeData

cd)

Returns a

ConfigurationInfo

object represented by the specified

CompositeData

.

The following table shows the required attributes that the specified

CompositeData

must contain.

Required names and types for CompositeData

Name

Type

name

String

label

String

description

String

provider

String

contents

String

settings

javax.management.openmbean.TabularData

with a

TabularType

with the keys

"key"

and

"value"

, both
of the

String

type

The following table shows the required attributes that the specified

CompositeData

must contain.

Required names and types for CompositeData

Name

Type

name

String

label

String

description

String

provider

String

contents

String

settings

javax.management.openmbean.TabularData

with a

TabularType

with the keys

"key"

and

"value"

, both
of the

String

type

toString

```java
public
String
toString()
```

Returns a description of the configuration that is associated with this

ConfigurationInfo

.

**Overrides:** toString

in class

Object
**Returns:** the description of the configuration, not

null

---

#### toString

public

String

toString()

Returns a description of the configuration that is associated with this

ConfigurationInfo

.

---

