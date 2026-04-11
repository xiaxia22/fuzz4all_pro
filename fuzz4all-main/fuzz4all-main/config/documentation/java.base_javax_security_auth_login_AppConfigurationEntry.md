# Class AppConfigurationEntry

**Source:** `java.base\javax\security\auth\login\AppConfigurationEntry.html`

### Class Description

```java
public class
AppConfigurationEntry

extends
Object
```

This class represents a single

LoginModule

entry
configured for the application specified in the

getAppConfigurationEntry(String appName)

method in the

Configuration

class. Each respective

AppConfigurationEntry

contains a

LoginModule

name,
a control flag (specifying whether this

LoginModule

is
REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL), and LoginModule-specific
options. Please refer to the

Configuration

class for
more information on the different control flags and their semantics.

**Since:** 1.4
**See Also:** Configuration

---

### Field Details

*No entries found.*

### Constructor Details

#### public AppConfigurationEntry​(
String
loginModuleName,

AppConfigurationEntry.LoginModuleControlFlag
controlFlag,

Map
<
String
,​?> options)

Default constructor for this class.

This entry represents a single

LoginModule

entry configured for the application specified in the

getAppConfigurationEntry(String appName)

method from the

Configuration

class.

**Parameters:**
- loginModuleName

- String representing the class name of the

LoginModule

configured for the
specified application.
- controlFlag

- either REQUIRED, REQUISITE, SUFFICIENT,
or OPTIONAL.
- options

- the options configured for this

LoginModule

.

**Throws:**
- IllegalArgumentException

- if

loginModuleName

is null, if

LoginModuleName

has a length of 0, if

controlFlag

is not either REQUIRED, REQUISITE, SUFFICIENT
or OPTIONAL, or if

options

is null.

---

### Method Details

#### public
String
getLoginModuleName()

Get the class name of the configured

LoginModule

.

**Returns:**
- the class name of the configured

LoginModule

as
a String.

---

#### public
AppConfigurationEntry.LoginModuleControlFlag
getControlFlag()

Return the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

**Returns:**
- the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

---

#### public
Map
<
String
,​?> getOptions()

Get the options configured for this

LoginModule

.

**Returns:**
- the options configured for this

LoginModule

as an unmodifiable

Map

.

---

### Additional Sections

#### Class AppConfigurationEntry

java.lang.Object

- javax.security.auth.login.AppConfigurationEntry

javax.security.auth.login.AppConfigurationEntry

```java
public class
AppConfigurationEntry

extends
Object
```

This class represents a single

LoginModule

entry
configured for the application specified in the

getAppConfigurationEntry(String appName)

method in the

Configuration

class. Each respective

AppConfigurationEntry

contains a

LoginModule

name,
a control flag (specifying whether this

LoginModule

is
REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL), and LoginModule-specific
options. Please refer to the

Configuration

class for
more information on the different control flags and their semantics.

**Since:** 1.4
**See Also:** Configuration

public class

AppConfigurationEntry

extends

Object

This class represents a single

LoginModule

entry
configured for the application specified in the

getAppConfigurationEntry(String appName)

method in the

Configuration

class. Each respective

AppConfigurationEntry

contains a

LoginModule

name,
a control flag (specifying whether this

LoginModule

is
REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL), and LoginModule-specific
options. Please refer to the

Configuration

class for
more information on the different control flags and their semantics.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

AppConfigurationEntry.LoginModuleControlFlag

This class represents whether or not a

LoginModule

is REQUIRED, REQUISITE, SUFFICIENT or OPTIONAL.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AppConfigurationEntry

​(

String

loginModuleName,

AppConfigurationEntry.LoginModuleControlFlag

controlFlag,

Map

<

String

,​?> options)

Default constructor for this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AppConfigurationEntry.LoginModuleControlFlag

getControlFlag

()

Return the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

String

getLoginModuleName

()

Get the class name of the configured

LoginModule

.

Map

<

String

,​?>

getOptions

()

Get the options configured for this

LoginModule

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

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

AppConfigurationEntry.LoginModuleControlFlag

This class represents whether or not a

LoginModule

is REQUIRED, REQUISITE, SUFFICIENT or OPTIONAL.

---

#### Nested Class Summary

This class represents whether or not a

LoginModule

is REQUIRED, REQUISITE, SUFFICIENT or OPTIONAL.

Constructor Summary

Constructors

Constructor

Description

AppConfigurationEntry

​(

String

loginModuleName,

AppConfigurationEntry.LoginModuleControlFlag

controlFlag,

Map

<

String

,​?> options)

Default constructor for this class.

---

#### Constructor Summary

Default constructor for this class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AppConfigurationEntry.LoginModuleControlFlag

getControlFlag

()

Return the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

String

getLoginModuleName

()

Get the class name of the configured

LoginModule

.

Map

<

String

,​?>

getOptions

()

Get the options configured for this

LoginModule

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Return the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

Get the class name of the configured

LoginModule

.

Get the options configured for this

LoginModule

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

toString

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

- AppConfigurationEntry

```java
public AppConfigurationEntry​(
String
loginModuleName,

AppConfigurationEntry.LoginModuleControlFlag
controlFlag,

Map
<
String
,​?> options)
```

Default constructor for this class.

This entry represents a single

LoginModule

entry configured for the application specified in the

getAppConfigurationEntry(String appName)

method from the

Configuration

class.

**Parameters:** loginModuleName

- String representing the class name of the

LoginModule

configured for the
specified application.
**Parameters:** controlFlag

- either REQUIRED, REQUISITE, SUFFICIENT,
or OPTIONAL.
**Parameters:** options

- the options configured for this

LoginModule

.
**Throws:** IllegalArgumentException

- if

loginModuleName

is null, if

LoginModuleName

has a length of 0, if

controlFlag

is not either REQUIRED, REQUISITE, SUFFICIENT
or OPTIONAL, or if

options

is null.

============ METHOD DETAIL ==========

- Method Detail

- getLoginModuleName

```java
public
String
getLoginModuleName()
```

Get the class name of the configured

LoginModule

.

**Returns:** the class name of the configured

LoginModule

as
a String.

- getControlFlag

```java
public
AppConfigurationEntry.LoginModuleControlFlag
getControlFlag()
```

Return the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

**Returns:** the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

- getOptions

```java
public
Map
<
String
,​?> getOptions()
```

Get the options configured for this

LoginModule

.

**Returns:** the options configured for this

LoginModule

as an unmodifiable

Map

.

Constructor Detail

- AppConfigurationEntry

```java
public AppConfigurationEntry​(
String
loginModuleName,

AppConfigurationEntry.LoginModuleControlFlag
controlFlag,

Map
<
String
,​?> options)
```

Default constructor for this class.

This entry represents a single

LoginModule

entry configured for the application specified in the

getAppConfigurationEntry(String appName)

method from the

Configuration

class.

**Parameters:** loginModuleName

- String representing the class name of the

LoginModule

configured for the
specified application.
**Parameters:** controlFlag

- either REQUIRED, REQUISITE, SUFFICIENT,
or OPTIONAL.
**Parameters:** options

- the options configured for this

LoginModule

.
**Throws:** IllegalArgumentException

- if

loginModuleName

is null, if

LoginModuleName

has a length of 0, if

controlFlag

is not either REQUIRED, REQUISITE, SUFFICIENT
or OPTIONAL, or if

options

is null.

---

#### Constructor Detail

AppConfigurationEntry

```java
public AppConfigurationEntry​(
String
loginModuleName,

AppConfigurationEntry.LoginModuleControlFlag
controlFlag,

Map
<
String
,​?> options)
```

Default constructor for this class.

This entry represents a single

LoginModule

entry configured for the application specified in the

getAppConfigurationEntry(String appName)

method from the

Configuration

class.

**Parameters:** loginModuleName

- String representing the class name of the

LoginModule

configured for the
specified application.
**Parameters:** controlFlag

- either REQUIRED, REQUISITE, SUFFICIENT,
or OPTIONAL.
**Parameters:** options

- the options configured for this

LoginModule

.
**Throws:** IllegalArgumentException

- if

loginModuleName

is null, if

LoginModuleName

has a length of 0, if

controlFlag

is not either REQUIRED, REQUISITE, SUFFICIENT
or OPTIONAL, or if

options

is null.

---

#### AppConfigurationEntry

public AppConfigurationEntry​(

String

loginModuleName,

AppConfigurationEntry.LoginModuleControlFlag

controlFlag,

Map

<

String

,​?> options)

Default constructor for this class.

This entry represents a single

LoginModule

entry configured for the application specified in the

getAppConfigurationEntry(String appName)

method from the

Configuration

class.

This entry represents a single

LoginModule

entry configured for the application specified in the

getAppConfigurationEntry(String appName)

method from the

Configuration

class.

Method Detail

- getLoginModuleName

```java
public
String
getLoginModuleName()
```

Get the class name of the configured

LoginModule

.

**Returns:** the class name of the configured

LoginModule

as
a String.

- getControlFlag

```java
public
AppConfigurationEntry.LoginModuleControlFlag
getControlFlag()
```

Return the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

**Returns:** the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

- getOptions

```java
public
Map
<
String
,​?> getOptions()
```

Get the options configured for this

LoginModule

.

**Returns:** the options configured for this

LoginModule

as an unmodifiable

Map

.

---

#### Method Detail

getLoginModuleName

```java
public
String
getLoginModuleName()
```

Get the class name of the configured

LoginModule

.

**Returns:** the class name of the configured

LoginModule

as
a String.

---

#### getLoginModuleName

public

String

getLoginModuleName()

Get the class name of the configured

LoginModule

.

getControlFlag

```java
public
AppConfigurationEntry.LoginModuleControlFlag
getControlFlag()
```

Return the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

**Returns:** the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

---

#### getControlFlag

public

AppConfigurationEntry.LoginModuleControlFlag

getControlFlag()

Return the controlFlag
(either REQUIRED, REQUISITE, SUFFICIENT, or OPTIONAL)
for this

LoginModule

.

getOptions

```java
public
Map
<
String
,​?> getOptions()
```

Get the options configured for this

LoginModule

.

**Returns:** the options configured for this

LoginModule

as an unmodifiable

Map

.

---

#### getOptions

public

Map

<

String

,​?> getOptions()

Get the options configured for this

LoginModule

.

---

