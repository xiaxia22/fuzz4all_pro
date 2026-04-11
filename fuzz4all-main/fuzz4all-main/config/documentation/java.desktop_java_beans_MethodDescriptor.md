# Class MethodDescriptor

**Source:** `java.desktop\java\beans\MethodDescriptor.html`

### Class Description

```java
public class
MethodDescriptor

extends
FeatureDescriptor
```

A MethodDescriptor describes a particular method that a Java Bean
supports for external access from other components.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

#### public MethodDescriptor​(
Method
method)

Constructs a

MethodDescriptor

from a

Method

.

**Parameters:**
- method

- The low-level method information.

---

#### public MethodDescriptor​(
Method
method,

ParameterDescriptor
[] parameterDescriptors)

Constructs a

MethodDescriptor

from a

Method

providing descriptive information for each
of the method's parameters.

**Parameters:**
- method

- The low-level method information.
- parameterDescriptors

- Descriptive information for each of the
method's parameters.

---

### Method Details

#### public
Method
getMethod()

Gets the method that this MethodDescriptor encapsulates.

**Returns:**
- The low-level description of the method

---

#### public
ParameterDescriptor
[] getParameterDescriptors()

Gets the ParameterDescriptor for each of this MethodDescriptor's
method's parameters.

**Returns:**
- The locale-independent names of the parameters. May return
a null array if the parameter names aren't known.

---

### Additional Sections

#### Class MethodDescriptor

java.lang.Object

- java.beans.FeatureDescriptor
- - java.beans.MethodDescriptor

java.beans.FeatureDescriptor

- java.beans.MethodDescriptor

java.beans.MethodDescriptor

```java
public class
MethodDescriptor

extends
FeatureDescriptor
```

A MethodDescriptor describes a particular method that a Java Bean
supports for external access from other components.

**Since:** 1.1

public class

MethodDescriptor

extends

FeatureDescriptor

A MethodDescriptor describes a particular method that a Java Bean
supports for external access from other components.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MethodDescriptor

​(

Method

method)

Constructs a

MethodDescriptor

from a

Method

.

MethodDescriptor

​(

Method

method,

ParameterDescriptor

[] parameterDescriptors)

Constructs a

MethodDescriptor

from a

Method

providing descriptive information for each
of the method's parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Method

getMethod

()

Gets the method that this MethodDescriptor encapsulates.

ParameterDescriptor

[]

getParameterDescriptors

()

Gets the ParameterDescriptor for each of this MethodDescriptor's
method's parameters.

- Methods declared in class java.beans.

FeatureDescriptor

attributeNames

,

getDisplayName

,

getName

,

getShortDescription

,

getValue

,

isExpert

,

isHidden

,

isPreferred

,

setDisplayName

,

setExpert

,

setHidden

,

setName

,

setPreferred

,

setShortDescription

,

setValue

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

Constructor

Description

MethodDescriptor

​(

Method

method)

Constructs a

MethodDescriptor

from a

Method

.

MethodDescriptor

​(

Method

method,

ParameterDescriptor

[] parameterDescriptors)

Constructs a

MethodDescriptor

from a

Method

providing descriptive information for each
of the method's parameters.

---

#### Constructor Summary

Constructs a

MethodDescriptor

from a

Method

.

Constructs a

MethodDescriptor

from a

Method

providing descriptive information for each
of the method's parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Method

getMethod

()

Gets the method that this MethodDescriptor encapsulates.

ParameterDescriptor

[]

getParameterDescriptors

()

Gets the ParameterDescriptor for each of this MethodDescriptor's
method's parameters.

- Methods declared in class java.beans.

FeatureDescriptor

attributeNames

,

getDisplayName

,

getName

,

getShortDescription

,

getValue

,

isExpert

,

isHidden

,

isPreferred

,

setDisplayName

,

setExpert

,

setHidden

,

setName

,

setPreferred

,

setShortDescription

,

setValue

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

Gets the method that this MethodDescriptor encapsulates.

Gets the ParameterDescriptor for each of this MethodDescriptor's
method's parameters.

Methods declared in class java.beans.

FeatureDescriptor

attributeNames

,

getDisplayName

,

getName

,

getShortDescription

,

getValue

,

isExpert

,

isHidden

,

isPreferred

,

setDisplayName

,

setExpert

,

setHidden

,

setName

,

setPreferred

,

setShortDescription

,

setValue

,

toString

---

#### Methods declared in class java.beans. FeatureDescriptor

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

- MethodDescriptor

```java
public MethodDescriptor​(
Method
method)
```

Constructs a

MethodDescriptor

from a

Method

.

**Parameters:** method

- The low-level method information.

- MethodDescriptor

```java
public MethodDescriptor​(
Method
method,

ParameterDescriptor
[] parameterDescriptors)
```

Constructs a

MethodDescriptor

from a

Method

providing descriptive information for each
of the method's parameters.

**Parameters:** method

- The low-level method information.
**Parameters:** parameterDescriptors

- Descriptive information for each of the
method's parameters.

============ METHOD DETAIL ==========

- Method Detail

- getMethod

```java
public
Method
getMethod()
```

Gets the method that this MethodDescriptor encapsulates.

**Returns:** The low-level description of the method

- getParameterDescriptors

```java
public
ParameterDescriptor
[] getParameterDescriptors()
```

Gets the ParameterDescriptor for each of this MethodDescriptor's
method's parameters.

**Returns:** The locale-independent names of the parameters. May return
a null array if the parameter names aren't known.

Constructor Detail

- MethodDescriptor

```java
public MethodDescriptor​(
Method
method)
```

Constructs a

MethodDescriptor

from a

Method

.

**Parameters:** method

- The low-level method information.

- MethodDescriptor

```java
public MethodDescriptor​(
Method
method,

ParameterDescriptor
[] parameterDescriptors)
```

Constructs a

MethodDescriptor

from a

Method

providing descriptive information for each
of the method's parameters.

**Parameters:** method

- The low-level method information.
**Parameters:** parameterDescriptors

- Descriptive information for each of the
method's parameters.

---

#### Constructor Detail

MethodDescriptor

```java
public MethodDescriptor​(
Method
method)
```

Constructs a

MethodDescriptor

from a

Method

.

**Parameters:** method

- The low-level method information.

---

#### MethodDescriptor

public MethodDescriptor​(

Method

method)

Constructs a

MethodDescriptor

from a

Method

.

MethodDescriptor

```java
public MethodDescriptor​(
Method
method,

ParameterDescriptor
[] parameterDescriptors)
```

Constructs a

MethodDescriptor

from a

Method

providing descriptive information for each
of the method's parameters.

**Parameters:** method

- The low-level method information.
**Parameters:** parameterDescriptors

- Descriptive information for each of the
method's parameters.

---

#### MethodDescriptor

public MethodDescriptor​(

Method

method,

ParameterDescriptor

[] parameterDescriptors)

Constructs a

MethodDescriptor

from a

Method

providing descriptive information for each
of the method's parameters.

Method Detail

- getMethod

```java
public
Method
getMethod()
```

Gets the method that this MethodDescriptor encapsulates.

**Returns:** The low-level description of the method

- getParameterDescriptors

```java
public
ParameterDescriptor
[] getParameterDescriptors()
```

Gets the ParameterDescriptor for each of this MethodDescriptor's
method's parameters.

**Returns:** The locale-independent names of the parameters. May return
a null array if the parameter names aren't known.

---

#### Method Detail

getMethod

```java
public
Method
getMethod()
```

Gets the method that this MethodDescriptor encapsulates.

**Returns:** The low-level description of the method

---

#### getMethod

public

Method

getMethod()

Gets the method that this MethodDescriptor encapsulates.

getParameterDescriptors

```java
public
ParameterDescriptor
[] getParameterDescriptors()
```

Gets the ParameterDescriptor for each of this MethodDescriptor's
method's parameters.

**Returns:** The locale-independent names of the parameters. May return
a null array if the parameter names aren't known.

---

#### getParameterDescriptors

public

ParameterDescriptor

[] getParameterDescriptors()

Gets the ParameterDescriptor for each of this MethodDescriptor's
method's parameters.

---

