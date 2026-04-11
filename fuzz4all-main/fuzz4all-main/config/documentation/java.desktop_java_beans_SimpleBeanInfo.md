# Class SimpleBeanInfo

**Source:** `java.desktop\java\beans\SimpleBeanInfo.html`

### Class Description

```java
public class
SimpleBeanInfo

extends
Object

implements
BeanInfo
```

This is a support class to make it easier for people to provide
BeanInfo classes.

It defaults to providing "noop" information, and can be selectively
overriden to provide more explicit information on chosen topics.
When the introspector sees the "noop" values, it will apply low
level introspection and design patterns to automatically analyze
the target bean.

**All Implemented Interfaces:** BeanInfo

---

### Field Details

*No entries found.*

### Constructor Details

#### public SimpleBeanInfo()

*No description found.*

---

### Method Details

#### public
BeanDescriptor
getBeanDescriptor()

Deny knowledge about the class and customizer of the bean.
You can override this if you wish to provide explicit info.

**Specified by:**
- getBeanDescriptor

in interface

BeanInfo

**Returns:**
- a

BeanDescriptor

object,
or

null

if the information is to
be obtained through the automatic analysis

---

#### public
PropertyDescriptor
[] getPropertyDescriptors()

Deny knowledge of properties. You can override this
if you wish to provide explicit property info.

**Specified by:**
- getPropertyDescriptors

in interface

BeanInfo

**Returns:**
- an array of

PropertyDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

---

#### public int getDefaultPropertyIndex()

Deny knowledge of a default property. You can override this
if you wish to define a default property for the bean.

**Specified by:**
- getDefaultPropertyIndex

in interface

BeanInfo

**Returns:**
- index of the default property in the

PropertyDescriptor

array
returned by the

getPropertyDescriptors

method,
or -1 if there is no default property

---

#### public
EventSetDescriptor
[] getEventSetDescriptors()

Deny knowledge of event sets. You can override this
if you wish to provide explicit event set info.

**Specified by:**
- getEventSetDescriptors

in interface

BeanInfo

**Returns:**
- an array of

EventSetDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

---

#### public int getDefaultEventIndex()

Deny knowledge of a default event. You can override this
if you wish to define a default event for the bean.

**Specified by:**
- getDefaultEventIndex

in interface

BeanInfo

**Returns:**
- index of the default event in the

EventSetDescriptor

array
returned by the

getEventSetDescriptors

method,
or -1 if there is no default event

---

#### public
MethodDescriptor
[] getMethodDescriptors()

Deny knowledge of methods. You can override this
if you wish to provide explicit method info.

**Specified by:**
- getMethodDescriptors

in interface

BeanInfo

**Returns:**
- an array of

MethodDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

---

#### public
BeanInfo
[] getAdditionalBeanInfo()

Claim there are no other relevant BeanInfo objects. You
may override this if you want to (for example) return a
BeanInfo for a base class.

**Specified by:**
- getAdditionalBeanInfo

in interface

BeanInfo

**Returns:**
- an array of

BeanInfo

objects,
or

null

if there are no additional

BeanInfo

objects

---

#### public
Image
getIcon​(int iconKind)

Claim there are no icons available. You can override
this if you want to provide icons for your bean.

**Specified by:**
- getIcon

in interface

BeanInfo

**Parameters:**
- iconKind

- the kind of icon requested

**Returns:**
- an image object representing the requested icon,
or

null

if no suitable icon is available

**See Also:**
- BeanInfo.ICON_COLOR_16x16

,

BeanInfo.ICON_COLOR_32x32

,

BeanInfo.ICON_MONO_16x16

,

BeanInfo.ICON_MONO_32x32

---

#### public
Image
loadImage​(
String
resourceName)

This is a utility method to help in loading icon images. It takes the
name of a resource file associated with the current object's class file
and loads an image object from that file. Typically images will be GIFs.

**Parameters:**
- resourceName

- A pathname relative to the directory holding the
class file of the current class. For example, "wombat.gif".

**Returns:**
- an image object or null if the resource is not found or the
resource could not be loaded as an Image

---

### Additional Sections

#### Class SimpleBeanInfo

java.lang.Object

- java.beans.SimpleBeanInfo

java.beans.SimpleBeanInfo

**All Implemented Interfaces:** BeanInfo

```java
public class
SimpleBeanInfo

extends
Object

implements
BeanInfo
```

This is a support class to make it easier for people to provide
BeanInfo classes.

It defaults to providing "noop" information, and can be selectively
overriden to provide more explicit information on chosen topics.
When the introspector sees the "noop" values, it will apply low
level introspection and design patterns to automatically analyze
the target bean.

**Since:** 1.1

public class

SimpleBeanInfo

extends

Object

implements

BeanInfo

This is a support class to make it easier for people to provide
BeanInfo classes.

It defaults to providing "noop" information, and can be selectively
overriden to provide more explicit information on chosen topics.
When the introspector sees the "noop" values, it will apply low
level introspection and design patterns to automatically analyze
the target bean.

It defaults to providing "noop" information, and can be selectively
overriden to provide more explicit information on chosen topics.
When the introspector sees the "noop" values, it will apply low
level introspection and design patterns to automatically analyze
the target bean.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleBeanInfo

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BeanInfo

[]

getAdditionalBeanInfo

()

Claim there are no other relevant BeanInfo objects.

BeanDescriptor

getBeanDescriptor

()

Deny knowledge about the class and customizer of the bean.

int

getDefaultEventIndex

()

Deny knowledge of a default event.

int

getDefaultPropertyIndex

()

Deny knowledge of a default property.

EventSetDescriptor

[]

getEventSetDescriptors

()

Deny knowledge of event sets.

Image

getIcon

​(int iconKind)

Claim there are no icons available.

MethodDescriptor

[]

getMethodDescriptors

()

Deny knowledge of methods.

PropertyDescriptor

[]

getPropertyDescriptors

()

Deny knowledge of properties.

Image

loadImage

​(

String

resourceName)

This is a utility method to help in loading icon images.

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

Constructor Summary

Constructors

Constructor

Description

SimpleBeanInfo

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BeanInfo

[]

getAdditionalBeanInfo

()

Claim there are no other relevant BeanInfo objects.

BeanDescriptor

getBeanDescriptor

()

Deny knowledge about the class and customizer of the bean.

int

getDefaultEventIndex

()

Deny knowledge of a default event.

int

getDefaultPropertyIndex

()

Deny knowledge of a default property.

EventSetDescriptor

[]

getEventSetDescriptors

()

Deny knowledge of event sets.

Image

getIcon

​(int iconKind)

Claim there are no icons available.

MethodDescriptor

[]

getMethodDescriptors

()

Deny knowledge of methods.

PropertyDescriptor

[]

getPropertyDescriptors

()

Deny knowledge of properties.

Image

loadImage

​(

String

resourceName)

This is a utility method to help in loading icon images.

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

Claim there are no other relevant BeanInfo objects.

Deny knowledge about the class and customizer of the bean.

Deny knowledge of a default event.

Deny knowledge of a default property.

Deny knowledge of event sets.

Claim there are no icons available.

Deny knowledge of methods.

Deny knowledge of properties.

This is a utility method to help in loading icon images.

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

- SimpleBeanInfo

```java
public SimpleBeanInfo()
```

============ METHOD DETAIL ==========

- Method Detail

- getBeanDescriptor

```java
public
BeanDescriptor
getBeanDescriptor()
```

Deny knowledge about the class and customizer of the bean.
You can override this if you wish to provide explicit info.

**Specified by:** getBeanDescriptor

in interface

BeanInfo
**Returns:** a

BeanDescriptor

object,
or

null

if the information is to
be obtained through the automatic analysis

- getPropertyDescriptors

```java
public
PropertyDescriptor
[] getPropertyDescriptors()
```

Deny knowledge of properties. You can override this
if you wish to provide explicit property info.

**Specified by:** getPropertyDescriptors

in interface

BeanInfo
**Returns:** an array of

PropertyDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

- getDefaultPropertyIndex

```java
public int getDefaultPropertyIndex()
```

Deny knowledge of a default property. You can override this
if you wish to define a default property for the bean.

**Specified by:** getDefaultPropertyIndex

in interface

BeanInfo
**Returns:** index of the default property in the

PropertyDescriptor

array
returned by the

getPropertyDescriptors

method,
or -1 if there is no default property

- getEventSetDescriptors

```java
public
EventSetDescriptor
[] getEventSetDescriptors()
```

Deny knowledge of event sets. You can override this
if you wish to provide explicit event set info.

**Specified by:** getEventSetDescriptors

in interface

BeanInfo
**Returns:** an array of

EventSetDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

- getDefaultEventIndex

```java
public int getDefaultEventIndex()
```

Deny knowledge of a default event. You can override this
if you wish to define a default event for the bean.

**Specified by:** getDefaultEventIndex

in interface

BeanInfo
**Returns:** index of the default event in the

EventSetDescriptor

array
returned by the

getEventSetDescriptors

method,
or -1 if there is no default event

- getMethodDescriptors

```java
public
MethodDescriptor
[] getMethodDescriptors()
```

Deny knowledge of methods. You can override this
if you wish to provide explicit method info.

**Specified by:** getMethodDescriptors

in interface

BeanInfo
**Returns:** an array of

MethodDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

- getAdditionalBeanInfo

```java
public
BeanInfo
[] getAdditionalBeanInfo()
```

Claim there are no other relevant BeanInfo objects. You
may override this if you want to (for example) return a
BeanInfo for a base class.

**Specified by:** getAdditionalBeanInfo

in interface

BeanInfo
**Returns:** an array of

BeanInfo

objects,
or

null

if there are no additional

BeanInfo

objects

- getIcon

```java
public
Image
getIcon​(int iconKind)
```

Claim there are no icons available. You can override
this if you want to provide icons for your bean.

**Specified by:** getIcon

in interface

BeanInfo
**Parameters:** iconKind

- the kind of icon requested
**Returns:** an image object representing the requested icon,
or

null

if no suitable icon is available
**See Also:** BeanInfo.ICON_COLOR_16x16

,

BeanInfo.ICON_COLOR_32x32

,

BeanInfo.ICON_MONO_16x16

,

BeanInfo.ICON_MONO_32x32

- loadImage

```java
public
Image
loadImage​(
String
resourceName)
```

This is a utility method to help in loading icon images. It takes the
name of a resource file associated with the current object's class file
and loads an image object from that file. Typically images will be GIFs.

**Parameters:** resourceName

- A pathname relative to the directory holding the
class file of the current class. For example, "wombat.gif".
**Returns:** an image object or null if the resource is not found or the
resource could not be loaded as an Image

Constructor Detail

- SimpleBeanInfo

```java
public SimpleBeanInfo()
```

---

#### Constructor Detail

SimpleBeanInfo

```java
public SimpleBeanInfo()
```

---

#### SimpleBeanInfo

public SimpleBeanInfo()

Method Detail

- getBeanDescriptor

```java
public
BeanDescriptor
getBeanDescriptor()
```

Deny knowledge about the class and customizer of the bean.
You can override this if you wish to provide explicit info.

**Specified by:** getBeanDescriptor

in interface

BeanInfo
**Returns:** a

BeanDescriptor

object,
or

null

if the information is to
be obtained through the automatic analysis

- getPropertyDescriptors

```java
public
PropertyDescriptor
[] getPropertyDescriptors()
```

Deny knowledge of properties. You can override this
if you wish to provide explicit property info.

**Specified by:** getPropertyDescriptors

in interface

BeanInfo
**Returns:** an array of

PropertyDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

- getDefaultPropertyIndex

```java
public int getDefaultPropertyIndex()
```

Deny knowledge of a default property. You can override this
if you wish to define a default property for the bean.

**Specified by:** getDefaultPropertyIndex

in interface

BeanInfo
**Returns:** index of the default property in the

PropertyDescriptor

array
returned by the

getPropertyDescriptors

method,
or -1 if there is no default property

- getEventSetDescriptors

```java
public
EventSetDescriptor
[] getEventSetDescriptors()
```

Deny knowledge of event sets. You can override this
if you wish to provide explicit event set info.

**Specified by:** getEventSetDescriptors

in interface

BeanInfo
**Returns:** an array of

EventSetDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

- getDefaultEventIndex

```java
public int getDefaultEventIndex()
```

Deny knowledge of a default event. You can override this
if you wish to define a default event for the bean.

**Specified by:** getDefaultEventIndex

in interface

BeanInfo
**Returns:** index of the default event in the

EventSetDescriptor

array
returned by the

getEventSetDescriptors

method,
or -1 if there is no default event

- getMethodDescriptors

```java
public
MethodDescriptor
[] getMethodDescriptors()
```

Deny knowledge of methods. You can override this
if you wish to provide explicit method info.

**Specified by:** getMethodDescriptors

in interface

BeanInfo
**Returns:** an array of

MethodDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

- getAdditionalBeanInfo

```java
public
BeanInfo
[] getAdditionalBeanInfo()
```

Claim there are no other relevant BeanInfo objects. You
may override this if you want to (for example) return a
BeanInfo for a base class.

**Specified by:** getAdditionalBeanInfo

in interface

BeanInfo
**Returns:** an array of

BeanInfo

objects,
or

null

if there are no additional

BeanInfo

objects

- getIcon

```java
public
Image
getIcon​(int iconKind)
```

Claim there are no icons available. You can override
this if you want to provide icons for your bean.

**Specified by:** getIcon

in interface

BeanInfo
**Parameters:** iconKind

- the kind of icon requested
**Returns:** an image object representing the requested icon,
or

null

if no suitable icon is available
**See Also:** BeanInfo.ICON_COLOR_16x16

,

BeanInfo.ICON_COLOR_32x32

,

BeanInfo.ICON_MONO_16x16

,

BeanInfo.ICON_MONO_32x32

- loadImage

```java
public
Image
loadImage​(
String
resourceName)
```

This is a utility method to help in loading icon images. It takes the
name of a resource file associated with the current object's class file
and loads an image object from that file. Typically images will be GIFs.

**Parameters:** resourceName

- A pathname relative to the directory holding the
class file of the current class. For example, "wombat.gif".
**Returns:** an image object or null if the resource is not found or the
resource could not be loaded as an Image

---

#### Method Detail

getBeanDescriptor

```java
public
BeanDescriptor
getBeanDescriptor()
```

Deny knowledge about the class and customizer of the bean.
You can override this if you wish to provide explicit info.

**Specified by:** getBeanDescriptor

in interface

BeanInfo
**Returns:** a

BeanDescriptor

object,
or

null

if the information is to
be obtained through the automatic analysis

---

#### getBeanDescriptor

public

BeanDescriptor

getBeanDescriptor()

Deny knowledge about the class and customizer of the bean.
You can override this if you wish to provide explicit info.

getPropertyDescriptors

```java
public
PropertyDescriptor
[] getPropertyDescriptors()
```

Deny knowledge of properties. You can override this
if you wish to provide explicit property info.

**Specified by:** getPropertyDescriptors

in interface

BeanInfo
**Returns:** an array of

PropertyDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

---

#### getPropertyDescriptors

public

PropertyDescriptor

[] getPropertyDescriptors()

Deny knowledge of properties. You can override this
if you wish to provide explicit property info.

getDefaultPropertyIndex

```java
public int getDefaultPropertyIndex()
```

Deny knowledge of a default property. You can override this
if you wish to define a default property for the bean.

**Specified by:** getDefaultPropertyIndex

in interface

BeanInfo
**Returns:** index of the default property in the

PropertyDescriptor

array
returned by the

getPropertyDescriptors

method,
or -1 if there is no default property

---

#### getDefaultPropertyIndex

public int getDefaultPropertyIndex()

Deny knowledge of a default property. You can override this
if you wish to define a default property for the bean.

getEventSetDescriptors

```java
public
EventSetDescriptor
[] getEventSetDescriptors()
```

Deny knowledge of event sets. You can override this
if you wish to provide explicit event set info.

**Specified by:** getEventSetDescriptors

in interface

BeanInfo
**Returns:** an array of

EventSetDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

---

#### getEventSetDescriptors

public

EventSetDescriptor

[] getEventSetDescriptors()

Deny knowledge of event sets. You can override this
if you wish to provide explicit event set info.

getDefaultEventIndex

```java
public int getDefaultEventIndex()
```

Deny knowledge of a default event. You can override this
if you wish to define a default event for the bean.

**Specified by:** getDefaultEventIndex

in interface

BeanInfo
**Returns:** index of the default event in the

EventSetDescriptor

array
returned by the

getEventSetDescriptors

method,
or -1 if there is no default event

---

#### getDefaultEventIndex

public int getDefaultEventIndex()

Deny knowledge of a default event. You can override this
if you wish to define a default event for the bean.

getMethodDescriptors

```java
public
MethodDescriptor
[] getMethodDescriptors()
```

Deny knowledge of methods. You can override this
if you wish to provide explicit method info.

**Specified by:** getMethodDescriptors

in interface

BeanInfo
**Returns:** an array of

MethodDescriptor

objects,
or

null

if the information is to
be obtained through the automatic analysis

---

#### getMethodDescriptors

public

MethodDescriptor

[] getMethodDescriptors()

Deny knowledge of methods. You can override this
if you wish to provide explicit method info.

getAdditionalBeanInfo

```java
public
BeanInfo
[] getAdditionalBeanInfo()
```

Claim there are no other relevant BeanInfo objects. You
may override this if you want to (for example) return a
BeanInfo for a base class.

**Specified by:** getAdditionalBeanInfo

in interface

BeanInfo
**Returns:** an array of

BeanInfo

objects,
or

null

if there are no additional

BeanInfo

objects

---

#### getAdditionalBeanInfo

public

BeanInfo

[] getAdditionalBeanInfo()

Claim there are no other relevant BeanInfo objects. You
may override this if you want to (for example) return a
BeanInfo for a base class.

getIcon

```java
public
Image
getIcon​(int iconKind)
```

Claim there are no icons available. You can override
this if you want to provide icons for your bean.

**Specified by:** getIcon

in interface

BeanInfo
**Parameters:** iconKind

- the kind of icon requested
**Returns:** an image object representing the requested icon,
or

null

if no suitable icon is available
**See Also:** BeanInfo.ICON_COLOR_16x16

,

BeanInfo.ICON_COLOR_32x32

,

BeanInfo.ICON_MONO_16x16

,

BeanInfo.ICON_MONO_32x32

---

#### getIcon

public

Image

getIcon​(int iconKind)

Claim there are no icons available. You can override
this if you want to provide icons for your bean.

loadImage

```java
public
Image
loadImage​(
String
resourceName)
```

This is a utility method to help in loading icon images. It takes the
name of a resource file associated with the current object's class file
and loads an image object from that file. Typically images will be GIFs.

**Parameters:** resourceName

- A pathname relative to the directory holding the
class file of the current class. For example, "wombat.gif".
**Returns:** an image object or null if the resource is not found or the
resource could not be loaded as an Image

---

#### loadImage

public

Image

loadImage​(

String

resourceName)

This is a utility method to help in loading icon images. It takes the
name of a resource file associated with the current object's class file
and loads an image object from that file. Typically images will be GIFs.

---

