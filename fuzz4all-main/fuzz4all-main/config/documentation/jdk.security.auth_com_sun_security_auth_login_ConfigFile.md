# Class ConfigFile

**Source:** `jdk.security.auth\com\sun\security\auth\login\ConfigFile.html`

### Class Description

```java
public class
ConfigFile

extends
Configuration
```

This class represents a default implementation for

javax.security.auth.login.Configuration

.

This object stores the runtime login configuration representation,
and is the amalgamation of multiple static login
configurations that resides in files.
The algorithm for locating the login configuration file(s) and reading their
information into this

Configuration

object is:

- Loop through the security properties,

login.config.url.1

,

login.config.url.2

, ...,

login.config.url.X

.
Each property value specifies a

URL

pointing to a
login configuration file to be loaded. Read in and load
each configuration.

The

java.lang.System

property

java.security.auth.login.config

may also be set to a

URL

pointing to another
login configuration file
(which is the case when a user uses the -D switch at runtime).
If this property is defined, and its use is allowed by the
security property file (the Security property,

policy.allowSystemProperty

is set to

true

),
also load that login configuration.

If the

java.security.auth.login.config

property is defined using
"==" (rather than "="), then ignore all other specified
login configurations and only load this configuration.

If no system or security properties were set, try to read from the file,
${user.home}/.java.login.config, where ${user.home} is the value
represented by the "user.home" System property.

The configuration syntax supported by this implementation
is exactly that syntax specified in the

javax.security.auth.login.Configuration

class.

**See Also:** LoginContext

,

security properties

---

### Field Details

*No entries found.*

### Constructor Details

#### public ConfigFile()

Create a new

Configuration

object.

**Throws:**
- SecurityException

- if the

Configuration

can not be
initialized

---

#### public ConfigFile​(
URI
uri)

Create a new

Configuration

object from the specified

URI

.

**Parameters:**
- uri

- the

URI

**Throws:**
- SecurityException

- if the

Configuration

can not be
initialized
- NullPointerException

- if

uri

is null

---

### Method Details

#### public
AppConfigurationEntry
[] getAppConfigurationEntry​(
String
applicationName)

Retrieve an entry from the

Configuration

using an application
name as an index.

**Specified by:**
- getAppConfigurationEntry

in class

Configuration

**Parameters:**
- applicationName

- the name used to index the

Configuration

**Returns:**
- an array of

AppConfigurationEntry

which correspond to
the stacked configuration of

LoginModule

s for this
application, or null if this application has no configured

LoginModule

s.

---

#### public void refresh()

Refresh and reload the

Configuration

by re-reading all of the
login configurations.

**Overrides:**
- refresh

in class

Configuration

**Throws:**
- SecurityException

- if the caller does not have permission
to refresh the

Configuration

---

### Additional Sections

#### Class ConfigFile

java.lang.Object

- javax.security.auth.login.Configuration
- - com.sun.security.auth.login.ConfigFile

javax.security.auth.login.Configuration

- com.sun.security.auth.login.ConfigFile

com.sun.security.auth.login.ConfigFile

```java
public class
ConfigFile

extends
Configuration
```

This class represents a default implementation for

javax.security.auth.login.Configuration

.

This object stores the runtime login configuration representation,
and is the amalgamation of multiple static login
configurations that resides in files.
The algorithm for locating the login configuration file(s) and reading their
information into this

Configuration

object is:

- Loop through the security properties,

login.config.url.1

,

login.config.url.2

, ...,

login.config.url.X

.
Each property value specifies a

URL

pointing to a
login configuration file to be loaded. Read in and load
each configuration.

The

java.lang.System

property

java.security.auth.login.config

may also be set to a

URL

pointing to another
login configuration file
(which is the case when a user uses the -D switch at runtime).
If this property is defined, and its use is allowed by the
security property file (the Security property,

policy.allowSystemProperty

is set to

true

),
also load that login configuration.

If the

java.security.auth.login.config

property is defined using
"==" (rather than "="), then ignore all other specified
login configurations and only load this configuration.

If no system or security properties were set, try to read from the file,
${user.home}/.java.login.config, where ${user.home} is the value
represented by the "user.home" System property.

The configuration syntax supported by this implementation
is exactly that syntax specified in the

javax.security.auth.login.Configuration

class.

**See Also:** LoginContext

,

security properties

public class

ConfigFile

extends

Configuration

This class represents a default implementation for

javax.security.auth.login.Configuration

.

This object stores the runtime login configuration representation,
and is the amalgamation of multiple static login
configurations that resides in files.
The algorithm for locating the login configuration file(s) and reading their
information into this

Configuration

object is:

- Loop through the security properties,

login.config.url.1

,

login.config.url.2

, ...,

login.config.url.X

.
Each property value specifies a

URL

pointing to a
login configuration file to be loaded. Read in and load
each configuration.

The

java.lang.System

property

java.security.auth.login.config

may also be set to a

URL

pointing to another
login configuration file
(which is the case when a user uses the -D switch at runtime).
If this property is defined, and its use is allowed by the
security property file (the Security property,

policy.allowSystemProperty

is set to

true

),
also load that login configuration.

If the

java.security.auth.login.config

property is defined using
"==" (rather than "="), then ignore all other specified
login configurations and only load this configuration.

If no system or security properties were set, try to read from the file,
${user.home}/.java.login.config, where ${user.home} is the value
represented by the "user.home" System property.

The configuration syntax supported by this implementation
is exactly that syntax specified in the

javax.security.auth.login.Configuration

class.

This object stores the runtime login configuration representation,
and is the amalgamation of multiple static login
configurations that resides in files.
The algorithm for locating the login configuration file(s) and reading their
information into this

Configuration

object is:

- Loop through the security properties,

login.config.url.1

,

login.config.url.2

, ...,

login.config.url.X

.
Each property value specifies a

URL

pointing to a
login configuration file to be loaded. Read in and load
each configuration.

The

java.lang.System

property

java.security.auth.login.config

may also be set to a

URL

pointing to another
login configuration file
(which is the case when a user uses the -D switch at runtime).
If this property is defined, and its use is allowed by the
security property file (the Security property,

policy.allowSystemProperty

is set to

true

),
also load that login configuration.

If the

java.security.auth.login.config

property is defined using
"==" (rather than "="), then ignore all other specified
login configurations and only load this configuration.

If no system or security properties were set, try to read from the file,
${user.home}/.java.login.config, where ${user.home} is the value
represented by the "user.home" System property.

The configuration syntax supported by this implementation
is exactly that syntax specified in the

javax.security.auth.login.Configuration

class.

Loop through the security properties,

login.config.url.1

,

login.config.url.2

, ...,

login.config.url.X

.
Each property value specifies a

URL

pointing to a
login configuration file to be loaded. Read in and load
each configuration.

The

java.lang.System

property

java.security.auth.login.config

may also be set to a

URL

pointing to another
login configuration file
(which is the case when a user uses the -D switch at runtime).
If this property is defined, and its use is allowed by the
security property file (the Security property,

policy.allowSystemProperty

is set to

true

),
also load that login configuration.

If the

java.security.auth.login.config

property is defined using
"==" (rather than "="), then ignore all other specified
login configurations and only load this configuration.

If no system or security properties were set, try to read from the file,
${user.home}/.java.login.config, where ${user.home} is the value
represented by the "user.home" System property.

The configuration syntax supported by this implementation
is exactly that syntax specified in the

javax.security.auth.login.Configuration

class.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.security.auth.login.

Configuration

Configuration.Parameters

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ConfigFile

()

Create a new

Configuration

object.

ConfigFile

​(

URI

uri)

Create a new

Configuration

object from the specified

URI

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AppConfigurationEntry

[]

getAppConfigurationEntry

​(

String

applicationName)

Retrieve an entry from the

Configuration

using an application
name as an index.

void

refresh

()

Refresh and reload the

Configuration

by re-reading all of the
login configurations.

- Methods declared in class javax.security.auth.login.

Configuration

getConfiguration

,

getInstance

,

getInstance

,

getInstance

,

getParameters

,

getProvider

,

getType

,

setConfiguration

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

- Nested classes/interfaces declared in class javax.security.auth.login.

Configuration

Configuration.Parameters

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.security.auth.login.

Configuration

Configuration.Parameters

---

#### Nested classes/interfaces declared in class javax.security.auth.login. Configuration

Constructor Summary

Constructors

Constructor

Description

ConfigFile

()

Create a new

Configuration

object.

ConfigFile

​(

URI

uri)

Create a new

Configuration

object from the specified

URI

.

---

#### Constructor Summary

Create a new

Configuration

object.

Create a new

Configuration

object from the specified

URI

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AppConfigurationEntry

[]

getAppConfigurationEntry

​(

String

applicationName)

Retrieve an entry from the

Configuration

using an application
name as an index.

void

refresh

()

Refresh and reload the

Configuration

by re-reading all of the
login configurations.

- Methods declared in class javax.security.auth.login.

Configuration

getConfiguration

,

getInstance

,

getInstance

,

getInstance

,

getParameters

,

getProvider

,

getType

,

setConfiguration

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

Retrieve an entry from the

Configuration

using an application
name as an index.

Refresh and reload the

Configuration

by re-reading all of the
login configurations.

Methods declared in class javax.security.auth.login.

Configuration

getConfiguration

,

getInstance

,

getInstance

,

getInstance

,

getParameters

,

getProvider

,

getType

,

setConfiguration

---

#### Methods declared in class javax.security.auth.login. Configuration

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

- ConfigFile

```java
public ConfigFile()
```

Create a new

Configuration

object.

**Throws:** SecurityException

- if the

Configuration

can not be
initialized

- ConfigFile

```java
public ConfigFile​(
URI
uri)
```

Create a new

Configuration

object from the specified

URI

.

**Parameters:** uri

- the

URI
**Throws:** SecurityException

- if the

Configuration

can not be
initialized
**Throws:** NullPointerException

- if

uri

is null

============ METHOD DETAIL ==========

- Method Detail

- getAppConfigurationEntry

```java
public
AppConfigurationEntry
[] getAppConfigurationEntry​(
String
applicationName)
```

Retrieve an entry from the

Configuration

using an application
name as an index.

**Specified by:** getAppConfigurationEntry

in class

Configuration
**Parameters:** applicationName

- the name used to index the

Configuration
**Returns:** an array of

AppConfigurationEntry

which correspond to
the stacked configuration of

LoginModule

s for this
application, or null if this application has no configured

LoginModule

s.

- refresh

```java
public void refresh()
```

Refresh and reload the

Configuration

by re-reading all of the
login configurations.

**Overrides:** refresh

in class

Configuration
**Throws:** SecurityException

- if the caller does not have permission
to refresh the

Configuration

Constructor Detail

- ConfigFile

```java
public ConfigFile()
```

Create a new

Configuration

object.

**Throws:** SecurityException

- if the

Configuration

can not be
initialized

- ConfigFile

```java
public ConfigFile​(
URI
uri)
```

Create a new

Configuration

object from the specified

URI

.

**Parameters:** uri

- the

URI
**Throws:** SecurityException

- if the

Configuration

can not be
initialized
**Throws:** NullPointerException

- if

uri

is null

---

#### Constructor Detail

ConfigFile

```java
public ConfigFile()
```

Create a new

Configuration

object.

**Throws:** SecurityException

- if the

Configuration

can not be
initialized

---

#### ConfigFile

public ConfigFile()

Create a new

Configuration

object.

ConfigFile

```java
public ConfigFile​(
URI
uri)
```

Create a new

Configuration

object from the specified

URI

.

**Parameters:** uri

- the

URI
**Throws:** SecurityException

- if the

Configuration

can not be
initialized
**Throws:** NullPointerException

- if

uri

is null

---

#### ConfigFile

public ConfigFile​(

URI

uri)

Create a new

Configuration

object from the specified

URI

.

Method Detail

- getAppConfigurationEntry

```java
public
AppConfigurationEntry
[] getAppConfigurationEntry​(
String
applicationName)
```

Retrieve an entry from the

Configuration

using an application
name as an index.

**Specified by:** getAppConfigurationEntry

in class

Configuration
**Parameters:** applicationName

- the name used to index the

Configuration
**Returns:** an array of

AppConfigurationEntry

which correspond to
the stacked configuration of

LoginModule

s for this
application, or null if this application has no configured

LoginModule

s.

- refresh

```java
public void refresh()
```

Refresh and reload the

Configuration

by re-reading all of the
login configurations.

**Overrides:** refresh

in class

Configuration
**Throws:** SecurityException

- if the caller does not have permission
to refresh the

Configuration

---

#### Method Detail

getAppConfigurationEntry

```java
public
AppConfigurationEntry
[] getAppConfigurationEntry​(
String
applicationName)
```

Retrieve an entry from the

Configuration

using an application
name as an index.

**Specified by:** getAppConfigurationEntry

in class

Configuration
**Parameters:** applicationName

- the name used to index the

Configuration
**Returns:** an array of

AppConfigurationEntry

which correspond to
the stacked configuration of

LoginModule

s for this
application, or null if this application has no configured

LoginModule

s.

---

#### getAppConfigurationEntry

public

AppConfigurationEntry

[] getAppConfigurationEntry​(

String

applicationName)

Retrieve an entry from the

Configuration

using an application
name as an index.

refresh

```java
public void refresh()
```

Refresh and reload the

Configuration

by re-reading all of the
login configurations.

**Overrides:** refresh

in class

Configuration
**Throws:** SecurityException

- if the caller does not have permission
to refresh the

Configuration

---

#### refresh

public void refresh()

Refresh and reload the

Configuration

by re-reading all of the
login configurations.

---

