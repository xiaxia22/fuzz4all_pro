# Class BeanDescriptor

**Source:** `java.desktop\java\beans\BeanDescriptor.html`

### Class Description

```java
public class
BeanDescriptor

extends
FeatureDescriptor
```

A BeanDescriptor provides global information about a "bean",
including its Java class, its displayName, etc.

This is one of the kinds of descriptor returned by a BeanInfo object,
which also returns descriptors for properties, method, and events.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

#### public BeanDescriptor​(
Class
<?> beanClass)

Create a BeanDescriptor for a bean that doesn't have a customizer.

**Parameters:**
- beanClass

- The Class object of the Java class that implements
the bean. For example sun.beans.OurButton.class.

---

#### public BeanDescriptor​(
Class
<?> beanClass,

Class
<?> customizerClass)

Create a BeanDescriptor for a bean that has a customizer.

**Parameters:**
- beanClass

- The Class object of the Java class that implements
the bean. For example sun.beans.OurButton.class.
- customizerClass

- The Class object of the Java class that implements
the bean's Customizer. For example sun.beans.OurButtonCustomizer.class.

---

### Method Details

#### public
Class
<?> getBeanClass()

Gets the bean's Class object.

**Returns:**
- The Class object for the bean.

---

#### public
Class
<?> getCustomizerClass()

Gets the Class object for the bean's customizer.

**Returns:**
- The Class object for the bean's customizer. This may
be null if the bean doesn't have a customizer.

---

### Additional Sections

#### Class BeanDescriptor

java.lang.Object

- java.beans.FeatureDescriptor
- - java.beans.BeanDescriptor

java.beans.FeatureDescriptor

- java.beans.BeanDescriptor

java.beans.BeanDescriptor

```java
public class
BeanDescriptor

extends
FeatureDescriptor
```

A BeanDescriptor provides global information about a "bean",
including its Java class, its displayName, etc.

This is one of the kinds of descriptor returned by a BeanInfo object,
which also returns descriptors for properties, method, and events.

**Since:** 1.1

public class

BeanDescriptor

extends

FeatureDescriptor

A BeanDescriptor provides global information about a "bean",
including its Java class, its displayName, etc.

This is one of the kinds of descriptor returned by a BeanInfo object,
which also returns descriptors for properties, method, and events.

This is one of the kinds of descriptor returned by a BeanInfo object,
which also returns descriptors for properties, method, and events.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BeanDescriptor

​(

Class

<?> beanClass)

Create a BeanDescriptor for a bean that doesn't have a customizer.

BeanDescriptor

​(

Class

<?> beanClass,

Class

<?> customizerClass)

Create a BeanDescriptor for a bean that has a customizer.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getBeanClass

()

Gets the bean's Class object.

Class

<?>

getCustomizerClass

()

Gets the Class object for the bean's customizer.

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

BeanDescriptor

​(

Class

<?> beanClass)

Create a BeanDescriptor for a bean that doesn't have a customizer.

BeanDescriptor

​(

Class

<?> beanClass,

Class

<?> customizerClass)

Create a BeanDescriptor for a bean that has a customizer.

---

#### Constructor Summary

Create a BeanDescriptor for a bean that doesn't have a customizer.

Create a BeanDescriptor for a bean that has a customizer.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getBeanClass

()

Gets the bean's Class object.

Class

<?>

getCustomizerClass

()

Gets the Class object for the bean's customizer.

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

Gets the bean's Class object.

Gets the Class object for the bean's customizer.

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

- BeanDescriptor

```java
public BeanDescriptor​(
Class
<?> beanClass)
```

Create a BeanDescriptor for a bean that doesn't have a customizer.

**Parameters:** beanClass

- The Class object of the Java class that implements
the bean. For example sun.beans.OurButton.class.

- BeanDescriptor

```java
public BeanDescriptor​(
Class
<?> beanClass,

Class
<?> customizerClass)
```

Create a BeanDescriptor for a bean that has a customizer.

**Parameters:** beanClass

- The Class object of the Java class that implements
the bean. For example sun.beans.OurButton.class.
**Parameters:** customizerClass

- The Class object of the Java class that implements
the bean's Customizer. For example sun.beans.OurButtonCustomizer.class.

============ METHOD DETAIL ==========

- Method Detail

- getBeanClass

```java
public
Class
<?> getBeanClass()
```

Gets the bean's Class object.

**Returns:** The Class object for the bean.

- getCustomizerClass

```java
public
Class
<?> getCustomizerClass()
```

Gets the Class object for the bean's customizer.

**Returns:** The Class object for the bean's customizer. This may
be null if the bean doesn't have a customizer.

Constructor Detail

- BeanDescriptor

```java
public BeanDescriptor​(
Class
<?> beanClass)
```

Create a BeanDescriptor for a bean that doesn't have a customizer.

**Parameters:** beanClass

- The Class object of the Java class that implements
the bean. For example sun.beans.OurButton.class.

- BeanDescriptor

```java
public BeanDescriptor​(
Class
<?> beanClass,

Class
<?> customizerClass)
```

Create a BeanDescriptor for a bean that has a customizer.

**Parameters:** beanClass

- The Class object of the Java class that implements
the bean. For example sun.beans.OurButton.class.
**Parameters:** customizerClass

- The Class object of the Java class that implements
the bean's Customizer. For example sun.beans.OurButtonCustomizer.class.

---

#### Constructor Detail

BeanDescriptor

```java
public BeanDescriptor​(
Class
<?> beanClass)
```

Create a BeanDescriptor for a bean that doesn't have a customizer.

**Parameters:** beanClass

- The Class object of the Java class that implements
the bean. For example sun.beans.OurButton.class.

---

#### BeanDescriptor

public BeanDescriptor​(

Class

<?> beanClass)

Create a BeanDescriptor for a bean that doesn't have a customizer.

BeanDescriptor

```java
public BeanDescriptor​(
Class
<?> beanClass,

Class
<?> customizerClass)
```

Create a BeanDescriptor for a bean that has a customizer.

**Parameters:** beanClass

- The Class object of the Java class that implements
the bean. For example sun.beans.OurButton.class.
**Parameters:** customizerClass

- The Class object of the Java class that implements
the bean's Customizer. For example sun.beans.OurButtonCustomizer.class.

---

#### BeanDescriptor

public BeanDescriptor​(

Class

<?> beanClass,

Class

<?> customizerClass)

Create a BeanDescriptor for a bean that has a customizer.

Method Detail

- getBeanClass

```java
public
Class
<?> getBeanClass()
```

Gets the bean's Class object.

**Returns:** The Class object for the bean.

- getCustomizerClass

```java
public
Class
<?> getCustomizerClass()
```

Gets the Class object for the bean's customizer.

**Returns:** The Class object for the bean's customizer. This may
be null if the bean doesn't have a customizer.

---

#### Method Detail

getBeanClass

```java
public
Class
<?> getBeanClass()
```

Gets the bean's Class object.

**Returns:** The Class object for the bean.

---

#### getBeanClass

public

Class

<?> getBeanClass()

Gets the bean's Class object.

getCustomizerClass

```java
public
Class
<?> getCustomizerClass()
```

Gets the Class object for the bean's customizer.

**Returns:** The Class object for the bean's customizer. This may
be null if the bean doesn't have a customizer.

---

#### getCustomizerClass

public

Class

<?> getCustomizerClass()

Gets the Class object for the bean's customizer.

---

