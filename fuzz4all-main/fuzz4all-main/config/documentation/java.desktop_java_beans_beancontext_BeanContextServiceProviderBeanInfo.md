# Interface BeanContextServiceProviderBeanInfo

**Source:** `java.desktop\java\beans\beancontext\BeanContextServiceProviderBeanInfo.html`

### Class Description

```java
public interface
BeanContextServiceProviderBeanInfo

extends
BeanInfo
```

A BeanContextServiceProvider implementor who wishes to provide explicit
information about the services their bean may provide shall implement a
BeanInfo class that implements this BeanInfo subinterface and provides
explicit information about the methods, properties, events, etc, of their
services.

**All Superinterfaces:** BeanInfo

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### BeanInfo
[] getServicesBeanInfo()

Gets a

BeanInfo

array, one for each
service class or interface statically available
from this ServiceProvider.

**Returns:**
- the

BeanInfo

array

---

### Additional Sections

#### Interface BeanContextServiceProviderBeanInfo

**All Superinterfaces:** BeanInfo

```java
public interface
BeanContextServiceProviderBeanInfo

extends
BeanInfo
```

A BeanContextServiceProvider implementor who wishes to provide explicit
information about the services their bean may provide shall implement a
BeanInfo class that implements this BeanInfo subinterface and provides
explicit information about the methods, properties, events, etc, of their
services.

public interface

BeanContextServiceProviderBeanInfo

extends

BeanInfo

A BeanContextServiceProvider implementor who wishes to provide explicit
information about the services their bean may provide shall implement a
BeanInfo class that implements this BeanInfo subinterface and provides
explicit information about the methods, properties, events, etc, of their
services.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.beans.

BeanInfo

ICON_COLOR_16x16

,

ICON_COLOR_32x32

,

ICON_MONO_16x16

,

ICON_MONO_32x32

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BeanInfo

[]

getServicesBeanInfo

()

Gets a

BeanInfo

array, one for each
service class or interface statically available
from this ServiceProvider.

- Methods declared in interface java.beans.

BeanInfo

getAdditionalBeanInfo

,

getBeanDescriptor

,

getDefaultEventIndex

,

getDefaultPropertyIndex

,

getEventSetDescriptors

,

getIcon

,

getMethodDescriptors

,

getPropertyDescriptors

Field Summary

- Fields declared in interface java.beans.

BeanInfo

ICON_COLOR_16x16

,

ICON_COLOR_32x32

,

ICON_MONO_16x16

,

ICON_MONO_32x32

---

#### Field Summary

Fields declared in interface java.beans.

BeanInfo

ICON_COLOR_16x16

,

ICON_COLOR_32x32

,

ICON_MONO_16x16

,

ICON_MONO_32x32

---

#### Fields declared in interface java.beans. BeanInfo

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BeanInfo

[]

getServicesBeanInfo

()

Gets a

BeanInfo

array, one for each
service class or interface statically available
from this ServiceProvider.

- Methods declared in interface java.beans.

BeanInfo

getAdditionalBeanInfo

,

getBeanDescriptor

,

getDefaultEventIndex

,

getDefaultPropertyIndex

,

getEventSetDescriptors

,

getIcon

,

getMethodDescriptors

,

getPropertyDescriptors

---

#### Method Summary

Gets a

BeanInfo

array, one for each
service class or interface statically available
from this ServiceProvider.

Methods declared in interface java.beans.

BeanInfo

getAdditionalBeanInfo

,

getBeanDescriptor

,

getDefaultEventIndex

,

getDefaultPropertyIndex

,

getEventSetDescriptors

,

getIcon

,

getMethodDescriptors

,

getPropertyDescriptors

---

#### Methods declared in interface java.beans. BeanInfo

============ METHOD DETAIL ==========

- Method Detail

- getServicesBeanInfo

```java
BeanInfo
[] getServicesBeanInfo()
```

Gets a

BeanInfo

array, one for each
service class or interface statically available
from this ServiceProvider.

**Returns:** the

BeanInfo

array

Method Detail

- getServicesBeanInfo

```java
BeanInfo
[] getServicesBeanInfo()
```

Gets a

BeanInfo

array, one for each
service class or interface statically available
from this ServiceProvider.

**Returns:** the

BeanInfo

array

---

#### Method Detail

getServicesBeanInfo

```java
BeanInfo
[] getServicesBeanInfo()
```

Gets a

BeanInfo

array, one for each
service class or interface statically available
from this ServiceProvider.

**Returns:** the

BeanInfo

array

---

#### getServicesBeanInfo

BeanInfo

[] getServicesBeanInfo()

Gets a

BeanInfo

array, one for each
service class or interface statically available
from this ServiceProvider.

---

