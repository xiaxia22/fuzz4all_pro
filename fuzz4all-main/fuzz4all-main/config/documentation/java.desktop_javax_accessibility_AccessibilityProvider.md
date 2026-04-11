# Class AccessibilityProvider

**Source:** `java.desktop\javax\accessibility\AccessibilityProvider.html`

### Class Description

```java
public abstract class
AccessibilityProvider

extends
Object
```

Service Provider Interface (SPI) for Assistive Technology.

This service provider class provides mappings from the platform specific
accessibility APIs to the Java Accessibility API.

Each service provider implementation is named and can be activated via the

activate()

method. Service providers can be loaded when the default

toolkit

is initialized.

**API Note:** There will typically be one provider per platform, such as Windows
or Linux, to support accessibility for screen readers and
magnifiers. However, more than one service provider can be
activated. For example, a test tool which provides visual results
obtained by interrogating the Java Accessibility API can be
activated along with the activation of the support for screen
readers and screen magnifiers.
**Since:** 9
**See Also:** Toolkit.getDefaultToolkit()

,

ServiceLoader

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AccessibilityProvider()

Initializes a new accessibility provider.

**Throws:**
- SecurityException

- If a security manager has been installed and it
denies

RuntimePermission

"accessibilityProvider"

---

### Method Details

#### public abstract
String
getName()

Returns the name of this service provider. This name is used to locate a
requested service provider.

**Returns:**
- the name of this service provider

---

#### public abstract void activate()

Activates the support provided by this service provider.

---

### Additional Sections

#### Class AccessibilityProvider

java.lang.Object

- javax.accessibility.AccessibilityProvider

javax.accessibility.AccessibilityProvider

```java
public abstract class
AccessibilityProvider

extends
Object
```

Service Provider Interface (SPI) for Assistive Technology.

This service provider class provides mappings from the platform specific
accessibility APIs to the Java Accessibility API.

Each service provider implementation is named and can be activated via the

activate()

method. Service providers can be loaded when the default

toolkit

is initialized.

**API Note:** There will typically be one provider per platform, such as Windows
or Linux, to support accessibility for screen readers and
magnifiers. However, more than one service provider can be
activated. For example, a test tool which provides visual results
obtained by interrogating the Java Accessibility API can be
activated along with the activation of the support for screen
readers and screen magnifiers.
**Since:** 9
**See Also:** Toolkit.getDefaultToolkit()

,

ServiceLoader

public abstract class

AccessibilityProvider

extends

Object

Service Provider Interface (SPI) for Assistive Technology.

This service provider class provides mappings from the platform specific
accessibility APIs to the Java Accessibility API.

Each service provider implementation is named and can be activated via the

activate()

method. Service providers can be loaded when the default

toolkit

is initialized.

This service provider class provides mappings from the platform specific
accessibility APIs to the Java Accessibility API.

Each service provider implementation is named and can be activated via the

activate()

method. Service providers can be loaded when the default

toolkit

is initialized.

Each service provider implementation is named and can be activated via the

activate()

method. Service providers can be loaded when the default

toolkit

is initialized.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AccessibilityProvider

()

Initializes a new accessibility provider.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

activate

()

Activates the support provided by this service provider.

abstract

String

getName

()

Returns the name of this service provider.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AccessibilityProvider

()

Initializes a new accessibility provider.

---

#### Constructor Summary

Initializes a new accessibility provider.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

activate

()

Activates the support provided by this service provider.

abstract

String

getName

()

Returns the name of this service provider.

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

Activates the support provided by this service provider.

Returns the name of this service provider.

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

- AccessibilityProvider

```java
protected AccessibilityProvider()
```

Initializes a new accessibility provider.

**Throws:** SecurityException

- If a security manager has been installed and it
denies

RuntimePermission

"accessibilityProvider"

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public abstract
String
getName()
```

Returns the name of this service provider. This name is used to locate a
requested service provider.

**Returns:** the name of this service provider

- activate

```java
public abstract void activate()
```

Activates the support provided by this service provider.

Constructor Detail

- AccessibilityProvider

```java
protected AccessibilityProvider()
```

Initializes a new accessibility provider.

**Throws:** SecurityException

- If a security manager has been installed and it
denies

RuntimePermission

"accessibilityProvider"

---

#### Constructor Detail

AccessibilityProvider

```java
protected AccessibilityProvider()
```

Initializes a new accessibility provider.

**Throws:** SecurityException

- If a security manager has been installed and it
denies

RuntimePermission

"accessibilityProvider"

---

#### AccessibilityProvider

protected AccessibilityProvider()

Initializes a new accessibility provider.

Method Detail

- getName

```java
public abstract
String
getName()
```

Returns the name of this service provider. This name is used to locate a
requested service provider.

**Returns:** the name of this service provider

- activate

```java
public abstract void activate()
```

Activates the support provided by this service provider.

---

#### Method Detail

getName

```java
public abstract
String
getName()
```

Returns the name of this service provider. This name is used to locate a
requested service provider.

**Returns:** the name of this service provider

---

#### getName

public abstract

String

getName()

Returns the name of this service provider. This name is used to locate a
requested service provider.

activate

```java
public abstract void activate()
```

Activates the support provided by this service provider.

---

#### activate

public abstract void activate()

Activates the support provided by this service provider.

---

