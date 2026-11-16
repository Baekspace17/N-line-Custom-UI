package com.baekspace.nline;

final class VehicleClientFactory {
    static VehiclePort create() { return new OemVehicleClient(); }

    static boolean simulated() { return false; }
}
