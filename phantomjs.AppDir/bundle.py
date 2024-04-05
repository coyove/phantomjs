ARCH = 'x86_64-linux-gnu'

a = [a.strip().replace('ARCH', ARCH) for a in """
/home/ubuntu/webkit-master/lib/libQt5WebKitWidgets.so.5
/home/ubuntu/webkit-master/lib/libQt5WebKit.so.5
/lib/ARCH/libQt5Network.so.5
/lib/ARCH/libQt5Widgets.so.5
/lib/ARCH/libQt5Gui.so.5
/lib/ARCH/libQt5Core.so.5
/lib/ARCH/libstdc++.so.6
/lib/ARCH/libm.so.6
/lib/ARCH/libgcc_s.so.1
/lib/ARCH/libz.so.1
/lib/ARCH/libgssapi_krb5.so.2
/lib/ARCH/libicudata.so.66
/lib/ARCH/libicui18n.so.66
/lib/ARCH/libicuuc.so.66
/lib/ARCH/libQt5Positioning.so.5
/lib/ARCH/libxml2.so.2
/lib/ARCH/libsqlite3.so.0
/lib/ARCH/libxslt.so.1
/lib/ARCH/libwoff2dec.so.1.0.2
/lib/ARCH/libpng16.so.16
/lib/ARCH/libwebpdemux.so.2
/lib/ARCH/libwebp.so.7
/lib/ARCH/libharfbuzz.so.0
/lib/ARCH/libharfbuzz-icu.so.0
/lib/ARCH/libfreetype.so.6
/lib/ARCH/libhyphen.so.0
/lib/ARCH/libtasn1.so.6
/lib/ARCH/libgcrypt.so.20
/lib/ARCH/libgpg-error.so.0
/lib/ARCH/libGL.so.1
/lib/ARCH/libmd4c.so.0
/lib/ARCH/libdouble-conversion.so.3
/lib/ARCH/libpcre2-16.so.0
/lib/ARCH/libzstd.so.1
/lib/ARCH/libglib-2.0.so.0
/lib/ARCH/libkrb5.so.3
/lib/ARCH/libk5crypto.so.3
/lib/ARCH/libcom_err.so.2
/lib/ARCH/libkrb5support.so.0
/lib/ARCH/liblzma.so.5
/lib/ARCH/libwoff2common.so.1.0.2
/lib/ARCH/libbrotlidec.so.1
/lib/ARCH/libgraphite2.so.3
/lib/ARCH/libGLdispatch.so.0
/lib/ARCH/libGLX.so.0
/lib/ARCH/libpcre.so.3
/lib/ARCH/libkeyutils.so.1
/lib/ARCH/libresolv.so.2
/lib/ARCH/libbrotlicommon.so.1
/lib/ARCH/libX11.so.6
/lib/ARCH/libxcb.so.1
/lib/ARCH/libXau.so.6
/lib/ARCH/libXdmcp.so.6
/lib/ARCH/libbsd.so.0
/lib/ARCH/libssl.so
/lib/ARCH/libssl.so.1.1
/lib/ARCH/libcrypto.so
/lib/ARCH/libcrypto.so.1.1
/lib/ARCH/libfontconfig.so.1
/lib/ARCH/libexpat.so.1
/lib/ARCH/libuuid.so.1
/lib/ARCH/libjpeg.so.8
/lib/ARCH/libQt5Svg.so.5
/lib/ARCH/libQt5DBus.so.5
/lib/ARCH/liblz4.so.1
/lib/ARCH/libdbus-1.so.3
/lib/ARCH/libcap.so.2
/lib/ARCH/libatomic.so.1
/lib/ARCH/libsharpyuv.so.0
/lib/ARCH/libsystemd.so.0
    """.split('\n') if a.strip()]

import re, os.path, shutil
from pathlib import Path

shutil.rmtree('lib', ignore_errors=True)
os.makedirs('lib', exist_ok=True)

for p in a:
    r = str(Path(p).resolve())
    dd = os.path.dirname(p)[1:]
    fn = os.path.basename(p)
    print(p, r)
    shutil.copyfile(r, 'lib/' + fn)

shutil.copytree('/usr/lib/' + ARCH + '/qt5/plugins', 'lib/plugins', dirs_exist_ok=True)
