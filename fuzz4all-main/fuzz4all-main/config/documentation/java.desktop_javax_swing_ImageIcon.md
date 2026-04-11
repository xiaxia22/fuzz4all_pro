# Class ImageIcon

**Source:** `java.desktop\javax\swing\ImageIcon.html`

### Class Description

```java
public class
ImageIcon

extends
Object

implements
Icon
,
Serializable
,
Accessible
```

An implementation of the Icon interface that paints Icons
from Images. Images that are created from a URL, filename or byte array
are preloaded using MediaTracker to monitor the loaded state
of the image.

For further information and examples of using image icons, see

How to Use Icons

in

The Java Tutorial.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

Accessible

,

Icon

---

### Field Details

#### @Deprecated

protected static final
Component
component

Do not use this shared component, which is used to track image loading.
It is left for backward compatibility only.

---

#### @Deprecated

protected static final
MediaTracker
tracker

Do not use this shared media tracker, which is used to load images.
It is left for backward compatibility only.

---

### Constructor Details

#### public ImageIcon​(
String
filename,

String
description)

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image.

**Parameters:**
- filename

- the name of the file containing the image
- description

- a brief textual description of the image

**See Also:**
- ImageIcon(String)

---

#### @ConstructorProperties
("description")
public ImageIcon​(
String
filename)

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image. The specified String can be a file name or a
file path. When specifying a path, use the Internet-standard
forward-slash ("/") as a separator.
(The string is converted to an URL, so the forward-slash works
on all systems.)
For example, specify:

```java
new ImageIcon("images/myImage.gif")
```

The description is initialized to the

filename

string.

**Parameters:**
- filename

- a String specifying a filename or path

**See Also:**
- getDescription()

---

#### public ImageIcon​(
URL
location,

String
description)

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.

**Parameters:**
- location

- the URL for the image
- description

- a brief textual description of the image

**See Also:**
- ImageIcon(String)

---

#### public ImageIcon​(
URL
location)

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.
The icon's description is initialized to be
a string representation of the URL.

**Parameters:**
- location

- the URL for the image

**See Also:**
- getDescription()

---

#### public ImageIcon​(
Image
image,

String
description)

Creates an ImageIcon from the image.

**Parameters:**
- image

- the image
- description

- a brief textual description of the image

---

#### public ImageIcon​(
Image
image)

Creates an ImageIcon from an image object.
If the image has a "comment" property that is a string,
then the string is used as the description of this icon.

**Parameters:**
- image

- the image

**See Also:**
- getDescription()

,

Image.getProperty(java.lang.String, java.awt.image.ImageObserver)

---

#### public ImageIcon​(byte[] imageData,

String
description)

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.

**Parameters:**
- imageData

- an array of pixels in an image format supported
by the AWT Toolkit, such as GIF, JPEG, or (as of 1.3) PNG
- description

- a brief textual description of the image

**See Also:**
- Toolkit.createImage(java.lang.String)

---

#### public ImageIcon​(byte[] imageData)

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.
If the resulting image has a "comment" property that is a string,
then the string is used as the description of this icon.

**Parameters:**
- imageData

- an array of pixels in an image format supported by
the AWT Toolkit, such as GIF, JPEG, or (as of 1.3) PNG

**See Also:**
- Toolkit.createImage(java.lang.String)

,

getDescription()

,

Image.getProperty(java.lang.String, java.awt.image.ImageObserver)

---

#### public ImageIcon()

Creates an uninitialized image icon.

---

### Method Details

#### protected void loadImage​(
Image
image)

Loads the image, returning only when the image is loaded.

**Parameters:**
- image

- the image

---

#### public int getImageLoadStatus()

Returns the status of the image loading operation.

**Returns:**
- the loading status as defined by java.awt.MediaTracker

**See Also:**
- MediaTracker.ABORTED

,

MediaTracker.ERRORED

,

MediaTracker.COMPLETE

---

#### public
Image
getImage()

Returns this icon's

Image

.

**Returns:**
- the

Image

object for this

ImageIcon

---

#### public void setImage​(
Image
image)

Sets the image displayed by this icon.

**Parameters:**
- image

- the image

---

#### public
String
getDescription()

Gets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.
The description may be null.

**Returns:**
- a brief textual description of the image

---

#### public void setDescription​(
String
description)

Sets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.

**Parameters:**
- description

- a brief textual description of the image

---

#### public void paintIcon​(
Component
c,

Graphics
g,
int x,
int y)

Paints the icon.
The top-left corner of the icon is drawn at
the point (

x

,

y

)
in the coordinate space of the graphics context

g

.
If this icon has no image observer,
this method uses the

c

component
as the observer.

**Specified by:**
- paintIcon

in interface

Icon

**Parameters:**
- c

- the component to be used as the observer
if this icon has no image observer
- g

- the graphics context
- x

- the X coordinate of the icon's top-left corner
- y

- the Y coordinate of the icon's top-left corner

---

#### public int getIconWidth()

Gets the width of the icon.

**Specified by:**
- getIconWidth

in interface

Icon

**Returns:**
- the width in pixels of this icon

---

#### public int getIconHeight()

Gets the height of the icon.

**Specified by:**
- getIconHeight

in interface

Icon

**Returns:**
- the height in pixels of this icon

---

#### public void setImageObserver​(
ImageObserver
observer)

Sets the image observer for the image. Set this
property if the ImageIcon contains an animated GIF, so
the observer is notified to update its display.
For example:

```java
icon = new ImageIcon(...)
button.setIcon(icon);
icon.setImageObserver(button);
```

**Parameters:**
- observer

- the image observer

---

#### public
ImageObserver
getImageObserver()

Returns the image observer for the image.

**Returns:**
- the image observer, which may be null

---

#### public
String
toString()

Returns a string representation of this image.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representing this image

---

#### @BeanProperty
(
expert
=true,

description
="The AccessibleContext associated with this ImageIcon.")
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this ImageIcon.
For image icons, the AccessibleContext takes the form of an
AccessibleImageIcon.
A new AccessibleImageIcon instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Returns:**
- an AccessibleImageIcon that serves as the
AccessibleContext of this ImageIcon

**Since:**
- 1.3

---

### Additional Sections

#### Class ImageIcon

java.lang.Object

- javax.swing.ImageIcon

javax.swing.ImageIcon

**All Implemented Interfaces:** Serializable

,

Accessible

,

Icon

```java
public class
ImageIcon

extends
Object

implements
Icon
,
Serializable
,
Accessible
```

An implementation of the Icon interface that paints Icons
from Images. Images that are created from a URL, filename or byte array
are preloaded using MediaTracker to monitor the loaded state
of the image.

For further information and examples of using image icons, see

How to Use Icons

in

The Java Tutorial.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.2
**See Also:** Serialized Form

public class

ImageIcon

extends

Object

implements

Icon

,

Serializable

,

Accessible

An implementation of the Icon interface that paints Icons
from Images. Images that are created from a URL, filename or byte array
are preloaded using MediaTracker to monitor the loaded state
of the image.

For further information and examples of using image icons, see

How to Use Icons

in

The Java Tutorial.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

For further information and examples of using image icons, see

How to Use Icons

in

The Java Tutorial.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

ImageIcon.AccessibleImageIcon

This class implements accessibility support for the

ImageIcon

class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static

Component

component

Deprecated.

since 1.8

protected static

MediaTracker

tracker

Deprecated.

since 1.8

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ImageIcon

()

Creates an uninitialized image icon.

ImageIcon

​(byte[] imageData)

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.

ImageIcon

​(byte[] imageData,

String

description)

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.

ImageIcon

​(

Image

image)

Creates an ImageIcon from an image object.

ImageIcon

​(

Image

image,

String

description)

Creates an ImageIcon from the image.

ImageIcon

​(

String

filename)

Creates an ImageIcon from the specified file.

ImageIcon

​(

String

filename,

String

description)

Creates an ImageIcon from the specified file.

ImageIcon

​(

URL

location)

Creates an ImageIcon from the specified URL.

ImageIcon

​(

URL

location,

String

description)

Creates an ImageIcon from the specified URL.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this ImageIcon.

String

getDescription

()

Gets the description of the image.

int

getIconHeight

()

Gets the height of the icon.

int

getIconWidth

()

Gets the width of the icon.

Image

getImage

()

Returns this icon's

Image

.

int

getImageLoadStatus

()

Returns the status of the image loading operation.

ImageObserver

getImageObserver

()

Returns the image observer for the image.

protected void

loadImage

​(

Image

image)

Loads the image, returning only when the image is loaded.

void

paintIcon

​(

Component

c,

Graphics

g,
int x,
int y)

Paints the icon.

void

setDescription

​(

String

description)

Sets the description of the image.

void

setImage

​(

Image

image)

Sets the image displayed by this icon.

void

setImageObserver

​(

ImageObserver

observer)

Sets the image observer for the image.

String

toString

()

Returns a string representation of this image.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

ImageIcon.AccessibleImageIcon

This class implements accessibility support for the

ImageIcon

class.

---

#### Nested Class Summary

This class implements accessibility support for the

ImageIcon

class.

Field Summary

Fields

Modifier and Type

Field

Description

protected static

Component

component

Deprecated.

since 1.8

protected static

MediaTracker

tracker

Deprecated.

since 1.8

---

#### Field Summary

Deprecated.

since 1.8

Constructor Summary

Constructors

Constructor

Description

ImageIcon

()

Creates an uninitialized image icon.

ImageIcon

​(byte[] imageData)

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.

ImageIcon

​(byte[] imageData,

String

description)

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.

ImageIcon

​(

Image

image)

Creates an ImageIcon from an image object.

ImageIcon

​(

Image

image,

String

description)

Creates an ImageIcon from the image.

ImageIcon

​(

String

filename)

Creates an ImageIcon from the specified file.

ImageIcon

​(

String

filename,

String

description)

Creates an ImageIcon from the specified file.

ImageIcon

​(

URL

location)

Creates an ImageIcon from the specified URL.

ImageIcon

​(

URL

location,

String

description)

Creates an ImageIcon from the specified URL.

---

#### Constructor Summary

Creates an uninitialized image icon.

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.

Creates an ImageIcon from an image object.

Creates an ImageIcon from the image.

Creates an ImageIcon from the specified file.

Creates an ImageIcon from the specified URL.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this ImageIcon.

String

getDescription

()

Gets the description of the image.

int

getIconHeight

()

Gets the height of the icon.

int

getIconWidth

()

Gets the width of the icon.

Image

getImage

()

Returns this icon's

Image

.

int

getImageLoadStatus

()

Returns the status of the image loading operation.

ImageObserver

getImageObserver

()

Returns the image observer for the image.

protected void

loadImage

​(

Image

image)

Loads the image, returning only when the image is loaded.

void

paintIcon

​(

Component

c,

Graphics

g,
int x,
int y)

Paints the icon.

void

setDescription

​(

String

description)

Sets the description of the image.

void

setImage

​(

Image

image)

Sets the image displayed by this icon.

void

setImageObserver

​(

ImageObserver

observer)

Sets the image observer for the image.

String

toString

()

Returns a string representation of this image.

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

Gets the AccessibleContext associated with this ImageIcon.

Gets the description of the image.

Gets the height of the icon.

Gets the width of the icon.

Returns this icon's

Image

.

Returns the status of the image loading operation.

Returns the image observer for the image.

Loads the image, returning only when the image is loaded.

Paints the icon.

Sets the description of the image.

Sets the image displayed by this icon.

Sets the image observer for the image.

Returns a string representation of this image.

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

============ FIELD DETAIL ===========

- Field Detail

- component

```java
@Deprecated

protected static final
Component
component
```

Deprecated.

since 1.8

Do not use this shared component, which is used to track image loading.
It is left for backward compatibility only.

- tracker

```java
@Deprecated

protected static final
MediaTracker
tracker
```

Deprecated.

since 1.8

Do not use this shared media tracker, which is used to load images.
It is left for backward compatibility only.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageIcon

```java
public ImageIcon​(
String
filename,

String
description)
```

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image.

**Parameters:** filename

- the name of the file containing the image
**Parameters:** description

- a brief textual description of the image
**See Also:** ImageIcon(String)

- ImageIcon

```java
@ConstructorProperties
("description")
public ImageIcon​(
String
filename)
```

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image. The specified String can be a file name or a
file path. When specifying a path, use the Internet-standard
forward-slash ("/") as a separator.
(The string is converted to an URL, so the forward-slash works
on all systems.)
For example, specify:

```java
new ImageIcon("images/myImage.gif")
```

The description is initialized to the

filename

string.

**Parameters:** filename

- a String specifying a filename or path
**See Also:** getDescription()

- ImageIcon

```java
public ImageIcon​(
URL
location,

String
description)
```

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.

**Parameters:** location

- the URL for the image
**Parameters:** description

- a brief textual description of the image
**See Also:** ImageIcon(String)

- ImageIcon

```java
public ImageIcon​(
URL
location)
```

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.
The icon's description is initialized to be
a string representation of the URL.

**Parameters:** location

- the URL for the image
**See Also:** getDescription()

- ImageIcon

```java
public ImageIcon​(
Image
image,

String
description)
```

Creates an ImageIcon from the image.

**Parameters:** image

- the image
**Parameters:** description

- a brief textual description of the image

- ImageIcon

```java
public ImageIcon​(
Image
image)
```

Creates an ImageIcon from an image object.
If the image has a "comment" property that is a string,
then the string is used as the description of this icon.

**Parameters:** image

- the image
**See Also:** getDescription()

,

Image.getProperty(java.lang.String, java.awt.image.ImageObserver)

- ImageIcon

```java
public ImageIcon​(byte[] imageData,

String
description)
```

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.

**Parameters:** imageData

- an array of pixels in an image format supported
by the AWT Toolkit, such as GIF, JPEG, or (as of 1.3) PNG
**Parameters:** description

- a brief textual description of the image
**See Also:** Toolkit.createImage(java.lang.String)

- ImageIcon

```java
public ImageIcon​(byte[] imageData)
```

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.
If the resulting image has a "comment" property that is a string,
then the string is used as the description of this icon.

**Parameters:** imageData

- an array of pixels in an image format supported by
the AWT Toolkit, such as GIF, JPEG, or (as of 1.3) PNG
**See Also:** Toolkit.createImage(java.lang.String)

,

getDescription()

,

Image.getProperty(java.lang.String, java.awt.image.ImageObserver)

- ImageIcon

```java
public ImageIcon()
```

Creates an uninitialized image icon.

============ METHOD DETAIL ==========

- Method Detail

- loadImage

```java
protected void loadImage​(
Image
image)
```

Loads the image, returning only when the image is loaded.

**Parameters:** image

- the image

- getImageLoadStatus

```java
public int getImageLoadStatus()
```

Returns the status of the image loading operation.

**Returns:** the loading status as defined by java.awt.MediaTracker
**See Also:** MediaTracker.ABORTED

,

MediaTracker.ERRORED

,

MediaTracker.COMPLETE

- getImage

```java
public
Image
getImage()
```

Returns this icon's

Image

.

**Returns:** the

Image

object for this

ImageIcon

- setImage

```java
public void setImage​(
Image
image)
```

Sets the image displayed by this icon.

**Parameters:** image

- the image

- getDescription

```java
public
String
getDescription()
```

Gets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.
The description may be null.

**Returns:** a brief textual description of the image

- setDescription

```java
public void setDescription​(
String
description)
```

Sets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.

**Parameters:** description

- a brief textual description of the image

- paintIcon

```java
public void paintIcon​(
Component
c,

Graphics
g,
int x,
int y)
```

Paints the icon.
The top-left corner of the icon is drawn at
the point (

x

,

y

)
in the coordinate space of the graphics context

g

.
If this icon has no image observer,
this method uses the

c

component
as the observer.

**Specified by:** paintIcon

in interface

Icon
**Parameters:** c

- the component to be used as the observer
if this icon has no image observer
**Parameters:** g

- the graphics context
**Parameters:** x

- the X coordinate of the icon's top-left corner
**Parameters:** y

- the Y coordinate of the icon's top-left corner

- getIconWidth

```java
public int getIconWidth()
```

Gets the width of the icon.

**Specified by:** getIconWidth

in interface

Icon
**Returns:** the width in pixels of this icon

- getIconHeight

```java
public int getIconHeight()
```

Gets the height of the icon.

**Specified by:** getIconHeight

in interface

Icon
**Returns:** the height in pixels of this icon

- setImageObserver

```java
public void setImageObserver​(
ImageObserver
observer)
```

Sets the image observer for the image. Set this
property if the ImageIcon contains an animated GIF, so
the observer is notified to update its display.
For example:

```java
icon = new ImageIcon(...)
button.setIcon(icon);
icon.setImageObserver(button);
```

**Parameters:** observer

- the image observer

- getImageObserver

```java
public
ImageObserver
getImageObserver()
```

Returns the image observer for the image.

**Returns:** the image observer, which may be null

- toString

```java
public
String
toString()
```

Returns a string representation of this image.

**Overrides:** toString

in class

Object
**Returns:** a string representing this image

- getAccessibleContext

```java
@BeanProperty
(
expert
=true,

description
="The AccessibleContext associated with this ImageIcon.")
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this ImageIcon.
For image icons, the AccessibleContext takes the form of an
AccessibleImageIcon.
A new AccessibleImageIcon instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** an AccessibleImageIcon that serves as the
AccessibleContext of this ImageIcon
**Since:** 1.3

Field Detail

- component

```java
@Deprecated

protected static final
Component
component
```

Deprecated.

since 1.8

Do not use this shared component, which is used to track image loading.
It is left for backward compatibility only.

- tracker

```java
@Deprecated

protected static final
MediaTracker
tracker
```

Deprecated.

since 1.8

Do not use this shared media tracker, which is used to load images.
It is left for backward compatibility only.

---

#### Field Detail

component

```java
@Deprecated

protected static final
Component
component
```

Deprecated.

since 1.8

Do not use this shared component, which is used to track image loading.
It is left for backward compatibility only.

---

#### component

@Deprecated

protected static final

Component

component

Do not use this shared component, which is used to track image loading.
It is left for backward compatibility only.

tracker

```java
@Deprecated

protected static final
MediaTracker
tracker
```

Deprecated.

since 1.8

Do not use this shared media tracker, which is used to load images.
It is left for backward compatibility only.

---

#### tracker

@Deprecated

protected static final

MediaTracker

tracker

Do not use this shared media tracker, which is used to load images.
It is left for backward compatibility only.

Constructor Detail

- ImageIcon

```java
public ImageIcon​(
String
filename,

String
description)
```

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image.

**Parameters:** filename

- the name of the file containing the image
**Parameters:** description

- a brief textual description of the image
**See Also:** ImageIcon(String)

- ImageIcon

```java
@ConstructorProperties
("description")
public ImageIcon​(
String
filename)
```

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image. The specified String can be a file name or a
file path. When specifying a path, use the Internet-standard
forward-slash ("/") as a separator.
(The string is converted to an URL, so the forward-slash works
on all systems.)
For example, specify:

```java
new ImageIcon("images/myImage.gif")
```

The description is initialized to the

filename

string.

**Parameters:** filename

- a String specifying a filename or path
**See Also:** getDescription()

- ImageIcon

```java
public ImageIcon​(
URL
location,

String
description)
```

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.

**Parameters:** location

- the URL for the image
**Parameters:** description

- a brief textual description of the image
**See Also:** ImageIcon(String)

- ImageIcon

```java
public ImageIcon​(
URL
location)
```

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.
The icon's description is initialized to be
a string representation of the URL.

**Parameters:** location

- the URL for the image
**See Also:** getDescription()

- ImageIcon

```java
public ImageIcon​(
Image
image,

String
description)
```

Creates an ImageIcon from the image.

**Parameters:** image

- the image
**Parameters:** description

- a brief textual description of the image

- ImageIcon

```java
public ImageIcon​(
Image
image)
```

Creates an ImageIcon from an image object.
If the image has a "comment" property that is a string,
then the string is used as the description of this icon.

**Parameters:** image

- the image
**See Also:** getDescription()

,

Image.getProperty(java.lang.String, java.awt.image.ImageObserver)

- ImageIcon

```java
public ImageIcon​(byte[] imageData,

String
description)
```

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.

**Parameters:** imageData

- an array of pixels in an image format supported
by the AWT Toolkit, such as GIF, JPEG, or (as of 1.3) PNG
**Parameters:** description

- a brief textual description of the image
**See Also:** Toolkit.createImage(java.lang.String)

- ImageIcon

```java
public ImageIcon​(byte[] imageData)
```

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.
If the resulting image has a "comment" property that is a string,
then the string is used as the description of this icon.

**Parameters:** imageData

- an array of pixels in an image format supported by
the AWT Toolkit, such as GIF, JPEG, or (as of 1.3) PNG
**See Also:** Toolkit.createImage(java.lang.String)

,

getDescription()

,

Image.getProperty(java.lang.String, java.awt.image.ImageObserver)

- ImageIcon

```java
public ImageIcon()
```

Creates an uninitialized image icon.

---

#### Constructor Detail

ImageIcon

```java
public ImageIcon​(
String
filename,

String
description)
```

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image.

**Parameters:** filename

- the name of the file containing the image
**Parameters:** description

- a brief textual description of the image
**See Also:** ImageIcon(String)

---

#### ImageIcon

public ImageIcon​(

String

filename,

String

description)

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image.

ImageIcon

```java
@ConstructorProperties
("description")
public ImageIcon​(
String
filename)
```

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image. The specified String can be a file name or a
file path. When specifying a path, use the Internet-standard
forward-slash ("/") as a separator.
(The string is converted to an URL, so the forward-slash works
on all systems.)
For example, specify:

```java
new ImageIcon("images/myImage.gif")
```

The description is initialized to the

filename

string.

**Parameters:** filename

- a String specifying a filename or path
**See Also:** getDescription()

---

#### ImageIcon

@ConstructorProperties

("description")
public ImageIcon​(

String

filename)

Creates an ImageIcon from the specified file. The image will
be preloaded by using MediaTracker to monitor the loading state
of the image. The specified String can be a file name or a
file path. When specifying a path, use the Internet-standard
forward-slash ("/") as a separator.
(The string is converted to an URL, so the forward-slash works
on all systems.)
For example, specify:

```java
new ImageIcon("images/myImage.gif")
```

The description is initialized to the

filename

string.

new ImageIcon("images/myImage.gif")

ImageIcon

```java
public ImageIcon​(
URL
location,

String
description)
```

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.

**Parameters:** location

- the URL for the image
**Parameters:** description

- a brief textual description of the image
**See Also:** ImageIcon(String)

---

#### ImageIcon

public ImageIcon​(

URL

location,

String

description)

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.

ImageIcon

```java
public ImageIcon​(
URL
location)
```

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.
The icon's description is initialized to be
a string representation of the URL.

**Parameters:** location

- the URL for the image
**See Also:** getDescription()

---

#### ImageIcon

public ImageIcon​(

URL

location)

Creates an ImageIcon from the specified URL. The image will
be preloaded by using MediaTracker to monitor the loaded state
of the image.
The icon's description is initialized to be
a string representation of the URL.

ImageIcon

```java
public ImageIcon​(
Image
image,

String
description)
```

Creates an ImageIcon from the image.

**Parameters:** image

- the image
**Parameters:** description

- a brief textual description of the image

---

#### ImageIcon

public ImageIcon​(

Image

image,

String

description)

Creates an ImageIcon from the image.

ImageIcon

```java
public ImageIcon​(
Image
image)
```

Creates an ImageIcon from an image object.
If the image has a "comment" property that is a string,
then the string is used as the description of this icon.

**Parameters:** image

- the image
**See Also:** getDescription()

,

Image.getProperty(java.lang.String, java.awt.image.ImageObserver)

---

#### ImageIcon

public ImageIcon​(

Image

image)

Creates an ImageIcon from an image object.
If the image has a "comment" property that is a string,
then the string is used as the description of this icon.

ImageIcon

```java
public ImageIcon​(byte[] imageData,

String
description)
```

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.

**Parameters:** imageData

- an array of pixels in an image format supported
by the AWT Toolkit, such as GIF, JPEG, or (as of 1.3) PNG
**Parameters:** description

- a brief textual description of the image
**See Also:** Toolkit.createImage(java.lang.String)

---

#### ImageIcon

public ImageIcon​(byte[] imageData,

String

description)

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.

ImageIcon

```java
public ImageIcon​(byte[] imageData)
```

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.
If the resulting image has a "comment" property that is a string,
then the string is used as the description of this icon.

**Parameters:** imageData

- an array of pixels in an image format supported by
the AWT Toolkit, such as GIF, JPEG, or (as of 1.3) PNG
**See Also:** Toolkit.createImage(java.lang.String)

,

getDescription()

,

Image.getProperty(java.lang.String, java.awt.image.ImageObserver)

---

#### ImageIcon

public ImageIcon​(byte[] imageData)

Creates an ImageIcon from an array of bytes which were
read from an image file containing a supported image format,
such as GIF, JPEG, or (as of 1.3) PNG.
Normally this array is created
by reading an image using Class.getResourceAsStream(), but
the byte array may also be statically stored in a class.
If the resulting image has a "comment" property that is a string,
then the string is used as the description of this icon.

ImageIcon

```java
public ImageIcon()
```

Creates an uninitialized image icon.

---

#### ImageIcon

public ImageIcon()

Creates an uninitialized image icon.

Method Detail

- loadImage

```java
protected void loadImage​(
Image
image)
```

Loads the image, returning only when the image is loaded.

**Parameters:** image

- the image

- getImageLoadStatus

```java
public int getImageLoadStatus()
```

Returns the status of the image loading operation.

**Returns:** the loading status as defined by java.awt.MediaTracker
**See Also:** MediaTracker.ABORTED

,

MediaTracker.ERRORED

,

MediaTracker.COMPLETE

- getImage

```java
public
Image
getImage()
```

Returns this icon's

Image

.

**Returns:** the

Image

object for this

ImageIcon

- setImage

```java
public void setImage​(
Image
image)
```

Sets the image displayed by this icon.

**Parameters:** image

- the image

- getDescription

```java
public
String
getDescription()
```

Gets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.
The description may be null.

**Returns:** a brief textual description of the image

- setDescription

```java
public void setDescription​(
String
description)
```

Sets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.

**Parameters:** description

- a brief textual description of the image

- paintIcon

```java
public void paintIcon​(
Component
c,

Graphics
g,
int x,
int y)
```

Paints the icon.
The top-left corner of the icon is drawn at
the point (

x

,

y

)
in the coordinate space of the graphics context

g

.
If this icon has no image observer,
this method uses the

c

component
as the observer.

**Specified by:** paintIcon

in interface

Icon
**Parameters:** c

- the component to be used as the observer
if this icon has no image observer
**Parameters:** g

- the graphics context
**Parameters:** x

- the X coordinate of the icon's top-left corner
**Parameters:** y

- the Y coordinate of the icon's top-left corner

- getIconWidth

```java
public int getIconWidth()
```

Gets the width of the icon.

**Specified by:** getIconWidth

in interface

Icon
**Returns:** the width in pixels of this icon

- getIconHeight

```java
public int getIconHeight()
```

Gets the height of the icon.

**Specified by:** getIconHeight

in interface

Icon
**Returns:** the height in pixels of this icon

- setImageObserver

```java
public void setImageObserver​(
ImageObserver
observer)
```

Sets the image observer for the image. Set this
property if the ImageIcon contains an animated GIF, so
the observer is notified to update its display.
For example:

```java
icon = new ImageIcon(...)
button.setIcon(icon);
icon.setImageObserver(button);
```

**Parameters:** observer

- the image observer

- getImageObserver

```java
public
ImageObserver
getImageObserver()
```

Returns the image observer for the image.

**Returns:** the image observer, which may be null

- toString

```java
public
String
toString()
```

Returns a string representation of this image.

**Overrides:** toString

in class

Object
**Returns:** a string representing this image

- getAccessibleContext

```java
@BeanProperty
(
expert
=true,

description
="The AccessibleContext associated with this ImageIcon.")
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this ImageIcon.
For image icons, the AccessibleContext takes the form of an
AccessibleImageIcon.
A new AccessibleImageIcon instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** an AccessibleImageIcon that serves as the
AccessibleContext of this ImageIcon
**Since:** 1.3

---

#### Method Detail

loadImage

```java
protected void loadImage​(
Image
image)
```

Loads the image, returning only when the image is loaded.

**Parameters:** image

- the image

---

#### loadImage

protected void loadImage​(

Image

image)

Loads the image, returning only when the image is loaded.

getImageLoadStatus

```java
public int getImageLoadStatus()
```

Returns the status of the image loading operation.

**Returns:** the loading status as defined by java.awt.MediaTracker
**See Also:** MediaTracker.ABORTED

,

MediaTracker.ERRORED

,

MediaTracker.COMPLETE

---

#### getImageLoadStatus

public int getImageLoadStatus()

Returns the status of the image loading operation.

getImage

```java
public
Image
getImage()
```

Returns this icon's

Image

.

**Returns:** the

Image

object for this

ImageIcon

---

#### getImage

public

Image

getImage()

Returns this icon's

Image

.

setImage

```java
public void setImage​(
Image
image)
```

Sets the image displayed by this icon.

**Parameters:** image

- the image

---

#### setImage

public void setImage​(

Image

image)

Sets the image displayed by this icon.

getDescription

```java
public
String
getDescription()
```

Gets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.
The description may be null.

**Returns:** a brief textual description of the image

---

#### getDescription

public

String

getDescription()

Gets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.
The description may be null.

setDescription

```java
public void setDescription​(
String
description)
```

Sets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.

**Parameters:** description

- a brief textual description of the image

---

#### setDescription

public void setDescription​(

String

description)

Sets the description of the image. This is meant to be a brief
textual description of the object. For example, it might be
presented to a blind user to give an indication of the purpose
of the image.

paintIcon

```java
public void paintIcon​(
Component
c,

Graphics
g,
int x,
int y)
```

Paints the icon.
The top-left corner of the icon is drawn at
the point (

x

,

y

)
in the coordinate space of the graphics context

g

.
If this icon has no image observer,
this method uses the

c

component
as the observer.

**Specified by:** paintIcon

in interface

Icon
**Parameters:** c

- the component to be used as the observer
if this icon has no image observer
**Parameters:** g

- the graphics context
**Parameters:** x

- the X coordinate of the icon's top-left corner
**Parameters:** y

- the Y coordinate of the icon's top-left corner

---

#### paintIcon

public void paintIcon​(

Component

c,

Graphics

g,
int x,
int y)

Paints the icon.
The top-left corner of the icon is drawn at
the point (

x

,

y

)
in the coordinate space of the graphics context

g

.
If this icon has no image observer,
this method uses the

c

component
as the observer.

getIconWidth

```java
public int getIconWidth()
```

Gets the width of the icon.

**Specified by:** getIconWidth

in interface

Icon
**Returns:** the width in pixels of this icon

---

#### getIconWidth

public int getIconWidth()

Gets the width of the icon.

getIconHeight

```java
public int getIconHeight()
```

Gets the height of the icon.

**Specified by:** getIconHeight

in interface

Icon
**Returns:** the height in pixels of this icon

---

#### getIconHeight

public int getIconHeight()

Gets the height of the icon.

setImageObserver

```java
public void setImageObserver​(
ImageObserver
observer)
```

Sets the image observer for the image. Set this
property if the ImageIcon contains an animated GIF, so
the observer is notified to update its display.
For example:

```java
icon = new ImageIcon(...)
button.setIcon(icon);
icon.setImageObserver(button);
```

**Parameters:** observer

- the image observer

---

#### setImageObserver

public void setImageObserver​(

ImageObserver

observer)

Sets the image observer for the image. Set this
property if the ImageIcon contains an animated GIF, so
the observer is notified to update its display.
For example:

```java
icon = new ImageIcon(...)
button.setIcon(icon);
icon.setImageObserver(button);
```

icon = new ImageIcon(...)
button.setIcon(icon);
icon.setImageObserver(button);

getImageObserver

```java
public
ImageObserver
getImageObserver()
```

Returns the image observer for the image.

**Returns:** the image observer, which may be null

---

#### getImageObserver

public

ImageObserver

getImageObserver()

Returns the image observer for the image.

toString

```java
public
String
toString()
```

Returns a string representation of this image.

**Overrides:** toString

in class

Object
**Returns:** a string representing this image

---

#### toString

public

String

toString()

Returns a string representation of this image.

getAccessibleContext

```java
@BeanProperty
(
expert
=true,

description
="The AccessibleContext associated with this ImageIcon.")
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this ImageIcon.
For image icons, the AccessibleContext takes the form of an
AccessibleImageIcon.
A new AccessibleImageIcon instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** an AccessibleImageIcon that serves as the
AccessibleContext of this ImageIcon
**Since:** 1.3

---

#### getAccessibleContext

@BeanProperty

(

expert

=true,

description

="The AccessibleContext associated with this ImageIcon.")
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this ImageIcon.
For image icons, the AccessibleContext takes the form of an
AccessibleImageIcon.
A new AccessibleImageIcon instance is created if necessary.

---

