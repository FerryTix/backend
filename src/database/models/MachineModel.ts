import * as mongoose from 'mongoose';
import { MachineLocation } from '../../models/MachineLocation';
import { model } from 'mongoose';

const MachineSchema = new mongoose.Schema({
  location: {
    type: Schema.Types,
    required: true
  },
  vending: Boolean,
  battery:
})

export default model("Machine", MachineSchema)
