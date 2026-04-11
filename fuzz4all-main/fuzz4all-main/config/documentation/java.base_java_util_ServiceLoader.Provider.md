# Interface ServiceLoader.Provider<S>

**Source:** `java.base\java\util\ServiceLoader.Provider.html`

### Class Description

```java
public static interface
ServiceLoader.Provider<S>

extends
Supplier
<S>
```

Represents a service provider located by

ServiceLoader

.

When using a loader's

stream()

method
then the elements are of type

Provider

. This allows processing
to select or filter on the provider class without instantiating the
provider.

**Type Parameters:** S

- The service type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Class
<? extends
S
> type()

Returns the provider type. There is no guarantee that this type is
accessible or that it has a public no-args constructor. The

get()

method should be used to obtain the provider instance.

When a module declares that the provider class is created by a
provider factory then this method returns the return type of its
public static "

provider()

" method.

**Returns:**
- The provider type

---

#### S
get()

Returns an instance of the provider.

**Specified by:**
- get

in interface

Supplier

<

S

>

**Returns:**
- An instance of the provider.

**Throws:**
- ServiceConfigurationError

- If the service provider cannot be instantiated, or in the
case of a provider factory, the public static
"

provider()

" method returns

null

or throws
an error or exception. The

ServiceConfigurationError

will carry an appropriate cause where possible.

---

### Additional Sections

#### Interface ServiceLoader.Provider<S>

**Type Parameters:** S

- The service type

**All Superinterfaces:** Supplier

<S>

**Enclosing class:** ServiceLoader

<

S

>

```java
public static interface
ServiceLoader.Provider<S>

extends
Supplier
<S>
```

Represents a service provider located by

ServiceLoader

.

When using a loader's

stream()

method
then the elements are of type

Provider

. This allows processing
to select or filter on the provider class without instantiating the
provider.

**Since:** 9

public static interface

ServiceLoader.Provider<S>

extends

Supplier

<S>

Represents a service provider located by

ServiceLoader

.

When using a loader's

stream()

method
then the elements are of type

Provider

. This allows processing
to select or filter on the provider class without instantiating the
provider.

When using a loader's

stream()

method
then the elements are of type

Provider

. This allows processing
to select or filter on the provider class without instantiating the
provider.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

S

get

()

Returns an instance of the provider.

Class

<? extends

S

>

type

()

Returns the provider type.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

S

get

()

Returns an instance of the provider.

Class

<? extends

S

>

type

()

Returns the provider type.

---

#### Method Summary

Returns an instance of the provider.

Returns the provider type.

============ METHOD DETAIL ==========

- Method Detail

- type

```java
Class
<? extends
S
> type()
```

Returns the provider type. There is no guarantee that this type is
accessible or that it has a public no-args constructor. The

get()

method should be used to obtain the provider instance.

When a module declares that the provider class is created by a
provider factory then this method returns the return type of its
public static "

provider()

" method.

**Returns:** The provider type

- get

```java
S
get()
```

Returns an instance of the provider.

**Specified by:** get

in interface

Supplier

<

S

>
**Returns:** An instance of the provider.
**Throws:** ServiceConfigurationError

- If the service provider cannot be instantiated, or in the
case of a provider factory, the public static
"

provider()

" method returns

null

or throws
an error or exception. The

ServiceConfigurationError

will carry an appropriate cause where possible.

Method Detail

- type

```java
Class
<? extends
S
> type()
```

Returns the provider type. There is no guarantee that this type is
accessible or that it has a public no-args constructor. The

get()

method should be used to obtain the provider instance.

When a module declares that the provider class is created by a
provider factory then this method returns the return type of its
public static "

provider()

" method.

**Returns:** The provider type

- get

```java
S
get()
```

Returns an instance of the provider.

**Specified by:** get

in interface

Supplier

<

S

>
**Returns:** An instance of the provider.
**Throws:** ServiceConfigurationError

- If the service provider cannot be instantiated, or in the
case of a provider factory, the public static
"

provider()

" method returns

null

or throws
an error or exception. The

ServiceConfigurationError

will carry an appropriate cause where possible.

---

#### Method Detail

type

```java
Class
<? extends
S
> type()
```

Returns the provider type. There is no guarantee that this type is
accessible or that it has a public no-args constructor. The

get()

method should be used to obtain the provider instance.

When a module declares that the provider class is created by a
provider factory then this method returns the return type of its
public static "

provider()

" method.

**Returns:** The provider type

---

#### type

Class

<? extends

S

> type()

Returns the provider type. There is no guarantee that this type is
accessible or that it has a public no-args constructor. The

get()

method should be used to obtain the provider instance.

When a module declares that the provider class is created by a
provider factory then this method returns the return type of its
public static "

provider()

" method.

When a module declares that the provider class is created by a
provider factory then this method returns the return type of its
public static "

provider()

" method.

get

```java
S
get()
```

Returns an instance of the provider.

**Specified by:** get

in interface

Supplier

<

S

>
**Returns:** An instance of the provider.
**Throws:** ServiceConfigurationError

- If the service provider cannot be instantiated, or in the
case of a provider factory, the public static
"

provider()

" method returns

null

or throws
an error or exception. The

ServiceConfigurationError

will carry an appropriate cause where possible.

---

#### get

S

get()

Returns an instance of the provider.

---

