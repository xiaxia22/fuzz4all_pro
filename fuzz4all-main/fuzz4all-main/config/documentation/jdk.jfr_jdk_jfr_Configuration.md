# Class Configuration

**Source:** `jdk.jfr\jdk\jfr\Configuration.html`

### Class Description

```java
public final class
Configuration

extends
Object
```

A collection of settings and metadata describing the configuration.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
Map
<
String
,​
String
> getSettings()

Returns the settings that specifies how a recording is configured.

Modifying the returned

Map

object doesn't change the
configuration.

**Returns:**
- settings, not

null

---

#### public
String
getName()

Returns an identifying name (for example,

"default" or "profile")

.

**Returns:**
- the name, or

null

if it doesn't exist

---

#### public
String
getLabel()

Returns a human-readable name (for example,

"Continuous" or "Profiling"

}.

**Returns:**
- the label, or

null

if it doesn't exist

---

#### public
String
getDescription()

Returns a short sentence that describes the configuration (for example

"Low
overhead configuration safe for continuous use in production
environments"

)

**Returns:**
- the description, or

null

if it doesn't exist

---

#### public
String
getProvider()

Returns who created the configuration (for example

"OpenJDK"

).

**Returns:**
- the provider, or

null

if it doesn't exist

---

#### public
String
getContents()

Returns a textual representation of the configuration (for example, the
contents of a JFC file).

**Returns:**
- contents, or

null

if it doesn't exist

**See Also:**
- getContents()

---

#### public static
Configuration
create​(
Path
path)
throws
IOException
,

ParseException

Reads a configuration from a file.

**Parameters:**
- path

- the file that contains the configuration, not

null

**Returns:**
- the read

Configuration

, not

null

**Throws:**
- ParseException

- if the file can't be parsed
- IOException

- if the file can't be read
- SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.

**See Also:**
- File.getPath()

,

SecurityManager.checkRead(java.lang.String)

---

#### public static
Configuration
create​(
Reader
reader)
throws
IOException
,

ParseException

Reads a configuration from a character stream.

**Parameters:**
- reader

- a

Reader

that provides the configuration contents, not

null

**Returns:**
- a configuration, not

null

**Throws:**
- IOException

- if an I/O error occurs while trying to read contents
from the

Reader
- ParseException

- if the file can't be parsed

---

#### public static
Configuration
getConfiguration​(
String
name)
throws
IOException
,

ParseException

Returns a predefined configuration.

See

getConfigurations()

for available configuration
names.

**Parameters:**
- name

- the name of the configuration (for example,

"default"

or

"profile"

)

**Returns:**
- a configuration, not

null

**Throws:**
- IOException

- if a configuration with the given name does not
exist, or if an I/O error occurs while reading the
configuration file
- ParseException

- if the configuration file can't be parsed

---

#### public static
List
<
Configuration
> getConfigurations()

Returns an immutable list of predefined configurations for this Java Virtual Machine (JVM).

**Returns:**
- the list of predefined configurations, not

null

---

### Additional Sections

#### Class Configuration

java.lang.Object

- jdk.jfr.Configuration

jdk.jfr.Configuration

```java
public final class
Configuration

extends
Object
```

A collection of settings and metadata describing the configuration.

**Since:** 9

public final class

Configuration

extends

Object

A collection of settings and metadata describing the configuration.

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

Configuration

create

​(

Reader

reader)

Reads a configuration from a character stream.

static

Configuration

create

​(

Path

path)

Reads a configuration from a file.

static

Configuration

getConfiguration

​(

String

name)

Returns a predefined configuration.

static

List

<

Configuration

>

getConfigurations

()

Returns an immutable list of predefined configurations for this Java Virtual Machine (JVM).

String

getContents

()

Returns a textual representation of the configuration (for example, the
contents of a JFC file).

String

getDescription

()

Returns a short sentence that describes the configuration (for example

"Low
overhead configuration safe for continuous use in production
environments"

)

String

getLabel

()

Returns a human-readable name (for example,

"Continuous" or "Profiling"

}.

String

getName

()

Returns an identifying name (for example,

"default" or "profile")

.

String

getProvider

()

Returns who created the configuration (for example

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

Returns the settings that specifies how a recording is configured.

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

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Configuration

create

​(

Reader

reader)

Reads a configuration from a character stream.

static

Configuration

create

​(

Path

path)

Reads a configuration from a file.

static

Configuration

getConfiguration

​(

String

name)

Returns a predefined configuration.

static

List

<

Configuration

>

getConfigurations

()

Returns an immutable list of predefined configurations for this Java Virtual Machine (JVM).

String

getContents

()

Returns a textual representation of the configuration (for example, the
contents of a JFC file).

String

getDescription

()

Returns a short sentence that describes the configuration (for example

"Low
overhead configuration safe for continuous use in production
environments"

)

String

getLabel

()

Returns a human-readable name (for example,

"Continuous" or "Profiling"

}.

String

getName

()

Returns an identifying name (for example,

"default" or "profile")

.

String

getProvider

()

Returns who created the configuration (for example

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

Returns the settings that specifies how a recording is configured.

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

Reads a configuration from a character stream.

Reads a configuration from a file.

Returns a predefined configuration.

Returns an immutable list of predefined configurations for this Java Virtual Machine (JVM).

Returns a textual representation of the configuration (for example, the
contents of a JFC file).

Returns a short sentence that describes the configuration (for example

"Low
overhead configuration safe for continuous use in production
environments"

)

Returns a human-readable name (for example,

"Continuous" or "Profiling"

}.

Returns an identifying name (for example,

"default" or "profile")

.

Returns who created the configuration (for example

"OpenJDK"

).

Returns the settings that specifies how a recording is configured.

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

Returns the settings that specifies how a recording is configured.

Modifying the returned

Map

object doesn't change the
configuration.

**Returns:** settings, not

null

- getName

```java
public
String
getName()
```

Returns an identifying name (for example,

"default" or "profile")

.

**Returns:** the name, or

null

if it doesn't exist

- getLabel

```java
public
String
getLabel()
```

Returns a human-readable name (for example,

"Continuous" or "Profiling"

}.

**Returns:** the label, or

null

if it doesn't exist

- getDescription

```java
public
String
getDescription()
```

Returns a short sentence that describes the configuration (for example

"Low
overhead configuration safe for continuous use in production
environments"

)

**Returns:** the description, or

null

if it doesn't exist

- getProvider

```java
public
String
getProvider()
```

Returns who created the configuration (for example

"OpenJDK"

).

**Returns:** the provider, or

null

if it doesn't exist

- getContents

```java
public
String
getContents()
```

Returns a textual representation of the configuration (for example, the
contents of a JFC file).

**Returns:** contents, or

null

if it doesn't exist
**See Also:** getContents()

- create

```java
public static
Configuration
create​(
Path
path)
throws
IOException
,

ParseException
```

Reads a configuration from a file.

**Parameters:** path

- the file that contains the configuration, not

null
**Returns:** the read

Configuration

, not

null
**Throws:** ParseException

- if the file can't be parsed
**Throws:** IOException

- if the file can't be read
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.
**See Also:** File.getPath()

,

SecurityManager.checkRead(java.lang.String)

- create

```java
public static
Configuration
create​(
Reader
reader)
throws
IOException
,

ParseException
```

Reads a configuration from a character stream.

**Parameters:** reader

- a

Reader

that provides the configuration contents, not

null
**Returns:** a configuration, not

null
**Throws:** IOException

- if an I/O error occurs while trying to read contents
from the

Reader
**Throws:** ParseException

- if the file can't be parsed

- getConfiguration

```java
public static
Configuration
getConfiguration​(
String
name)
throws
IOException
,

ParseException
```

Returns a predefined configuration.

See

getConfigurations()

for available configuration
names.

**Parameters:** name

- the name of the configuration (for example,

"default"

or

"profile"

)
**Returns:** a configuration, not

null
**Throws:** IOException

- if a configuration with the given name does not
exist, or if an I/O error occurs while reading the
configuration file
**Throws:** ParseException

- if the configuration file can't be parsed

- getConfigurations

```java
public static
List
<
Configuration
> getConfigurations()
```

Returns an immutable list of predefined configurations for this Java Virtual Machine (JVM).

**Returns:** the list of predefined configurations, not

null

Method Detail

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

Returns the settings that specifies how a recording is configured.

Modifying the returned

Map

object doesn't change the
configuration.

**Returns:** settings, not

null

- getName

```java
public
String
getName()
```

Returns an identifying name (for example,

"default" or "profile")

.

**Returns:** the name, or

null

if it doesn't exist

- getLabel

```java
public
String
getLabel()
```

Returns a human-readable name (for example,

"Continuous" or "Profiling"

}.

**Returns:** the label, or

null

if it doesn't exist

- getDescription

```java
public
String
getDescription()
```

Returns a short sentence that describes the configuration (for example

"Low
overhead configuration safe for continuous use in production
environments"

)

**Returns:** the description, or

null

if it doesn't exist

- getProvider

```java
public
String
getProvider()
```

Returns who created the configuration (for example

"OpenJDK"

).

**Returns:** the provider, or

null

if it doesn't exist

- getContents

```java
public
String
getContents()
```

Returns a textual representation of the configuration (for example, the
contents of a JFC file).

**Returns:** contents, or

null

if it doesn't exist
**See Also:** getContents()

- create

```java
public static
Configuration
create​(
Path
path)
throws
IOException
,

ParseException
```

Reads a configuration from a file.

**Parameters:** path

- the file that contains the configuration, not

null
**Returns:** the read

Configuration

, not

null
**Throws:** ParseException

- if the file can't be parsed
**Throws:** IOException

- if the file can't be read
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.
**See Also:** File.getPath()

,

SecurityManager.checkRead(java.lang.String)

- create

```java
public static
Configuration
create​(
Reader
reader)
throws
IOException
,

ParseException
```

Reads a configuration from a character stream.

**Parameters:** reader

- a

Reader

that provides the configuration contents, not

null
**Returns:** a configuration, not

null
**Throws:** IOException

- if an I/O error occurs while trying to read contents
from the

Reader
**Throws:** ParseException

- if the file can't be parsed

- getConfiguration

```java
public static
Configuration
getConfiguration​(
String
name)
throws
IOException
,

ParseException
```

Returns a predefined configuration.

See

getConfigurations()

for available configuration
names.

**Parameters:** name

- the name of the configuration (for example,

"default"

or

"profile"

)
**Returns:** a configuration, not

null
**Throws:** IOException

- if a configuration with the given name does not
exist, or if an I/O error occurs while reading the
configuration file
**Throws:** ParseException

- if the configuration file can't be parsed

- getConfigurations

```java
public static
List
<
Configuration
> getConfigurations()
```

Returns an immutable list of predefined configurations for this Java Virtual Machine (JVM).

**Returns:** the list of predefined configurations, not

null

---

#### Method Detail

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

Returns the settings that specifies how a recording is configured.

Modifying the returned

Map

object doesn't change the
configuration.

**Returns:** settings, not

null

---

#### getSettings

public

Map

<

String

,​

String

> getSettings()

Returns the settings that specifies how a recording is configured.

Modifying the returned

Map

object doesn't change the
configuration.

Modifying the returned

Map

object doesn't change the
configuration.

getName

```java
public
String
getName()
```

Returns an identifying name (for example,

"default" or "profile")

.

**Returns:** the name, or

null

if it doesn't exist

---

#### getName

public

String

getName()

Returns an identifying name (for example,

"default" or "profile")

.

getLabel

```java
public
String
getLabel()
```

Returns a human-readable name (for example,

"Continuous" or "Profiling"

}.

**Returns:** the label, or

null

if it doesn't exist

---

#### getLabel

public

String

getLabel()

Returns a human-readable name (for example,

"Continuous" or "Profiling"

}.

getDescription

```java
public
String
getDescription()
```

Returns a short sentence that describes the configuration (for example

"Low
overhead configuration safe for continuous use in production
environments"

)

**Returns:** the description, or

null

if it doesn't exist

---

#### getDescription

public

String

getDescription()

Returns a short sentence that describes the configuration (for example

"Low
overhead configuration safe for continuous use in production
environments"

)

getProvider

```java
public
String
getProvider()
```

Returns who created the configuration (for example

"OpenJDK"

).

**Returns:** the provider, or

null

if it doesn't exist

---

#### getProvider

public

String

getProvider()

Returns who created the configuration (for example

"OpenJDK"

).

getContents

```java
public
String
getContents()
```

Returns a textual representation of the configuration (for example, the
contents of a JFC file).

**Returns:** contents, or

null

if it doesn't exist
**See Also:** getContents()

---

#### getContents

public

String

getContents()

Returns a textual representation of the configuration (for example, the
contents of a JFC file).

create

```java
public static
Configuration
create​(
Path
path)
throws
IOException
,

ParseException
```

Reads a configuration from a file.

**Parameters:** path

- the file that contains the configuration, not

null
**Returns:** the read

Configuration

, not

null
**Throws:** ParseException

- if the file can't be parsed
**Throws:** IOException

- if the file can't be read
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.
**See Also:** File.getPath()

,

SecurityManager.checkRead(java.lang.String)

---

#### create

public static

Configuration

create​(

Path

path)
throws

IOException

,

ParseException

Reads a configuration from a file.

create

```java
public static
Configuration
create​(
Reader
reader)
throws
IOException
,

ParseException
```

Reads a configuration from a character stream.

**Parameters:** reader

- a

Reader

that provides the configuration contents, not

null
**Returns:** a configuration, not

null
**Throws:** IOException

- if an I/O error occurs while trying to read contents
from the

Reader
**Throws:** ParseException

- if the file can't be parsed

---

#### create

public static

Configuration

create​(

Reader

reader)
throws

IOException

,

ParseException

Reads a configuration from a character stream.

getConfiguration

```java
public static
Configuration
getConfiguration​(
String
name)
throws
IOException
,

ParseException
```

Returns a predefined configuration.

See

getConfigurations()

for available configuration
names.

**Parameters:** name

- the name of the configuration (for example,

"default"

or

"profile"

)
**Returns:** a configuration, not

null
**Throws:** IOException

- if a configuration with the given name does not
exist, or if an I/O error occurs while reading the
configuration file
**Throws:** ParseException

- if the configuration file can't be parsed

---

#### getConfiguration

public static

Configuration

getConfiguration​(

String

name)
throws

IOException

,

ParseException

Returns a predefined configuration.

See

getConfigurations()

for available configuration
names.

See

getConfigurations()

for available configuration
names.

getConfigurations

```java
public static
List
<
Configuration
> getConfigurations()
```

Returns an immutable list of predefined configurations for this Java Virtual Machine (JVM).

**Returns:** the list of predefined configurations, not

null

---

#### getConfigurations

public static

List

<

Configuration

> getConfigurations()

Returns an immutable list of predefined configurations for this Java Virtual Machine (JVM).

---

